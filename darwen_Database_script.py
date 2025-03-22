IS_CALLED = Relation(('StudentId', 'Name'),
[Tuple(StudentId='S1', Name='Anne'), Tuple(StudentId='S2', Name='Boris'), Tuple(StudentId='S3', Name='Cindy'), Tuple(StudentId='S4', Name='Devinder'), Tuple(StudentId='S5', Name='Boris')],
{'PK':(Key, None)})

IS_ENROLLED_ON = Relation(('StudentId', 'CourseId'),
[Tuple(StudentId='S1', CourseId='C1'), Tuple(StudentId='S1', CourseId='C2'), Tuple(StudentId='S2', CourseId='C1'), Tuple(StudentId='S3', CourseId='C3'), Tuple(StudentId='S4', CourseId='C1')],
{'PK':(Key, None)})

COURSE = Relation(('CourseId', 'Title'),
[Tuple(CourseId='C1', Title='Database'), Tuple(CourseId='C2', Title='HCI'), Tuple(CourseId='C3', Title='Op Systems'), Tuple(CourseId='C4', Title='Programming')],
{'PK':(Key, None)})

EXAM_MARK = Relation(('StudentId', 'CourseId', 'Mark'),
[Tuple(StudentId='S1', CourseId='C1', Mark=85), Tuple(StudentId='S1', CourseId='C2', Mark=49), Tuple(StudentId='S2', CourseId='C1', Mark=49), Tuple(StudentId='S3', CourseId='C3', Mark=66), Tuple(StudentId='S4', CourseId='C1', Mark=93)],
{'PK':(Key, None)})

