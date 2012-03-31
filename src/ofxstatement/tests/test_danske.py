import doctest

from ofxstatement.plugins.danske import DanskeCsvStatementParser

def doctest_DanskeCsvStatementParser():
    """Test DanskeCsvStatementParser

    Open sample csv to parse
        >>> import os
        >>> csvfile = os.path.join(os.path.dirname(__file__),
        ...                        'samples', 'danske.csv')


    Create parser and parse
        >>> fin = open(csvfile, 'r', encoding='cp1257')
        >>> parser = DanskeCsvStatementParser(fin)
        >>> statement = parser.parse()

    Check what we've got:
        >>> len(statement.lines)
        4
        >>> statement.startingBalance
        0.0
        >>> statement.endingBalance
        0.0
        >>> statement.startingBalanceDate
        datetime.datetime(2012, 3, 1, 0, 0)
        >>> statement.endingBalanceDate
        datetime.datetime(2012, 3, 7, 0, 0)

    First line is a payment for incoming transaction:
        >>> l = statement.lines[0]
        >>> l.amount
        -7.8
        >>> l.memo
        'Paslaugų ir komisinių pajamos už gaunamus tarptautinius pervedimus USD'
        >>> l.date
        datetime.datetime(2012, 3, 1, 0, 0)
        >>> l.id
        '8585175472216523258'

    Second line is incoming money
        >>> l = statement.lines[1]
        >>> l.amount
        889.81
        >>> l.memo
        'ACME LLC'
        >>> l.date
        datetime.datetime(2012, 3, 1, 0, 0)

    Third line is a pament with amount less than 1 USD
        >>> l = statement.lines[2]
        >>> l.amount
        -0.46
        >>> l.memo
        'Mokestis už lėšų, gautų iš kitų LR registruotų bankų, ... 2012.03.06'

    Fourth is a transfer to other account
        >>> l = statement.lines[3]
        >>> l.memo
        'John Doe'
        >>> l.amount
        -881.55
    """

def test_suite():
    return doctest.DocTestSuite(optionflags=(doctest.NORMALIZE_WHITESPACE|
                                             doctest.ELLIPSIS|
                                             doctest.REPORT_ONLY_FIRST_FAILURE|
                                             doctest.REPORT_NDIFF
                                             ))