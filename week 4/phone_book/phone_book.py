# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [None] * 10 ** 7
    for cur_query in queries:
        mhash = ((34 * cur_query.number + 2) % 10000019) % 10**7
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if contacts[mhash] is None:
                contacts[mhash] = cur_query
            elif contacts[mhash].number == cur_query.number:
                contacts[mhash].name = cur_query.name
        elif cur_query.type == 'del' and contacts[mhash] is not None:
            if contacts[mhash].number == cur_query.number:
                    contacts[mhash] = None
        elif cur_query.type == 'find':
            response = 'not found'
            if contacts[mhash] is not None:
                response = contacts[mhash].name
            result.append(response)
        else:
            continue
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

