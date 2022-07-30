def format_playlist(songs):
    empty_playlist = f"{'+'}{6*'-'}{'+'}{6*'-'}{'+'}{8*'-'}{'+'}\n"\
             f"|{'Name'.center(6)}|{'Time'.center(6)}|{'Artist'.center(8)}|\n"\
             f"{'+'}{6*'-'}{'+'}{6*'-'}{'+'}{8*'-'}{'+'}"
    if len(songs)==0:
        return empty_playlist
    else :
        max_name = int(max([len(i[0]) for i in songs]))
        max_time = int(max([len(i[1]) for i in songs]))
        max_artist = int(max([len(i[2]) for i in songs]))
        header =(f"{'+'}{(max_name+2)*'-'}{'+'}{(max_time+2)*'-'}{'+'}{(max_artist+2)*'-'}{'+'}\n"
                 f"|{' Name'.ljust(max_name+2)}|{' Time'.ljust(max_time+2)}|{' Artist'.ljust(max_artist+2)}|\n"
                 f"{'+'}{(max_name+2)*'-'}{'+'}{ (max_time+2)*'-'}{'+'}{(max_artist+2)*'-'}{'+'}\n")
        end = f"{'+'}{(max_name+2)*'-'}{'+'}{(max_time+2)*'-'}{'+'}{(max_artist+2)*'-'}{'+'}"
        s  = ''
        for i in songs:
            s += (f"{'|'}{' '+str(i[0]).ljust(max_name+1)}{'|'}{' '+str(i[1]).ljust(max_time+1)}{'|'}{' '+ str(i[2]).ljust(max_artist+1)}{'|'}\n")
        return(header+s+end)

songs = [
        ('In Da Club', '3:13', '50 Cent'),
        ('Candy Shop', '3:45', '50 Cent'),
        ('One', '4:36', 'U2'),
        ('Wicked', '2:53', 'Future'),
        ('Cellular', '2:58', 'King Krule'),
        ('The Birthday Party', '4:45', 'The 1975'),
        ('In The Night Of Wilderness', '5:26', 'Blackmill'),
        ('nnkPull Up', '333:35', 'Playboi Cartinlk'),
        ('Cudi Montage', '3:16', 'KIDS SEE GHOSTS'),
        ('What Up Gangsta', '2:58', '50 Cent')]
