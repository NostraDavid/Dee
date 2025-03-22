S = Relation(('S#', 'SNAME', 'STATUS', 'CITY'),
[Tuple(S#='S1', SNAME='Smith', STATUS=20, CITY='London'), Tuple(S#='S2', SNAME='Jones', STATUS=10, CITY='Paris'), Tuple(S#='S3', SNAME='Blake', STATUS=30, CITY='Paris'), Tuple(S#='S4', SNAME='Clark', STATUS=20, CITY='London'), Tuple(S#='S5', SNAME='Adams', STATUS=30, CITY='Athens')],
{'pk':(Key, ['S#'])})

P = Relation(('P#', 'PNAME', 'COLOR', 'WEIGHT', 'CITY'),
[Tuple(P#='P1', PNAME='Nut', COLOR='Red', WEIGHT=12, CITY='London'), Tuple(P#='P2', PNAME='Bolt', COLOR='Green', WEIGHT=17, CITY='Paris'), Tuple(P#='P3', PNAME='Screw', COLOR='Blue', WEIGHT=17, CITY='Rome'), Tuple(P#='P4', PNAME='Screw', COLOR='Red', WEIGHT=14, CITY='London'), Tuple(P#='P5', PNAME='Cam', COLOR='Blue', WEIGHT=12, CITY='Paris'), Tuple(P#='P6', PNAME='Cog', COLOR='Red', WEIGHT=19, CITY='London')],
{'pk':(Key, ['P#'])})

SP = Relation(('S#', 'P#', 'QTY'),
[Tuple(S#='S1', P#='P1', QTY=300), Tuple(S#='S1', P#='P2', QTY=200), Tuple(S#='S1', P#='P3', QTY=400), Tuple(S#='S1', P#='P4', QTY=200), Tuple(S#='S1', P#='P5', QTY=100), Tuple(S#='S1', P#='P6', QTY=100), Tuple(S#='S2', P#='P1', QTY=300), Tuple(S#='S2', P#='P2', QTY=400), Tuple(S#='S3', P#='P2', QTY=200), Tuple(S#='S4', P#='P2', QTY=200), Tuple(S#='S4', P#='P4', QTY=300), Tuple(S#='S4', P#='P5', QTY=400)],
{'pk':(Key, ['S#', 'P#']),
'fkS':(ForeignKey, ('S', {'S#': 'S#'})),
'fkP':(ForeignKey, ('P', {'P#': 'P#'}))})

