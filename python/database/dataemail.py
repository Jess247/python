import sqlite3
# creates a sqlite file if no file can be found
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

# get a file name loop through it
fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    ''' sample line from mbox file 'From (pieces 0) rjlowe@iupui.edu (pieces 1) Fri Jan  4 14:50:18 2008'
    '''
    if not line.startswith('From'):
        continue
    pieces = line.split()
    email = pieces[1]
    # to prevent SQL injections ? is used as a placeholder which will be
    # replaced by a single tuple (email)
    # opens a recordset
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    # get information from db
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                        VALUES (?,1)''', (email,))
    else:
        # increment the number
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
