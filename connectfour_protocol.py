from collections import namedtuple
import connectfour
import socket

#Some of these methods are the same methods I found in the Protocols notes.

PollingConnection = namedtuple("PollingConnection", ['socket', 'input', 'output'])

def connect(username, host, port):
    '''Connect to the server running on parameter host/port.'''

    polling_socket = socket.socket()
    
    polling_socket.connect((host, port))
    polling_input = polling_socket.makefile('r')
    polling_output = polling_socket.makefile('w')


    return PollingConnection(
        socket = polling_socket,
        input = polling_input,
        output = polling_output)


def userMove(connection, choice, col):
    '''Sends a user's move to the server.'''
    try:
        if choice.strip().upper() == 'DROP':
            writeline(connection, 'DROP ' + str(col))
        elif choice.strip().upper() == 'POP':
            writeline(connection, 'POP ' + str(col))
        response = readstream(connection)
        if response.startswith('INVALID'):
            response = readstream(connection)
            if not response.startswith('READY'):
                close(connection)
                return 'closed'
            return 'invalid'
        return response
    except:
        close(connection)
        return 'closed'
    

def serverMove(connection):
    '''Recieves a move from the server.'''
    ans = []
    try:
        response = readstream(connection)
        if response.startswith('DROP'):
            ans = ['DROP', int(response[4:].strip())]
        elif response.startswith('POP'):
            ans = ['POP', int(response[4:].strip())]
        else:
            close(connection)
            return 'closed'

        response = readstream(connection)
        if response.startswith('WINNER_RED') or response.startswith('WINNER_YELLOW'):
            close(connection)
        elif not response.startswith('READY'):
            close(connection)
            return 'closed'
        return ans
    except:
        close(connection)
        return 'closed'
            


def close(connection):
    '''Close the connection.'''
    connection.input.close()
    connection.output.close()
    connection.socket.close()

def readstream(connection):
    '''Read a line of text from the server and return without the newline.'''
    line = connection.input.readline()[:-1]
    return line


def writeline(connection, txt):
    '''Write a line of text to the server.'''
    connection.output.write(txt + '\r\n')
    connection.output.flush()
