"""
1. Find the one node that has no connection to outside nodes
   Make sure there's just one

2. Make sure all other nodes point to it
"""


def find_judge_beej(n, trust):
    trust_map = {}  # key is the truster, value is list of trustees
    # trusted_by_map = {}

    for truster, trustee in trust:
        if truster not in trust_map:
            trust_map[truster] = []

        trust_map[truster].append(trustee)

        """
        if trustee not in trusted_by_map:
            trusted_by_map[trustee] = []

        trusted_by_map[trustee].append(truster)
        """

    # Find the person who trusts nobody
    trusts_nobody = None

    for i in range(1, n + 1):
        if i not in trust_map:

            # print(f"{i} doesn't trust anyone")

            if trusts_nobody is not None:  # Too many people trust no one
                return -1

            trusts_nobody = i

    # This _might_ be the judge
    candidate = trusts_nobody;

    # Make sure everyone trusts the candidate
    for i in range(1, n + 1):
        if i == candidate:  # Except the judge doesn't have to trust themselves
            continue

        this_person_trusts = trust_map[i]

        if candidate not in this_person_trusts:
            return -1

    # if we get here, candidate is the judge
    return candidate


def judge_trust(n, trust):
    trust_in = {i: 0 for i in range(1, n + 1)}
    trust_out = {i: 0 for i in range(1, n + 1)}

    for truster, trustee in trust:
        trust_out[truster] += 1
        trust_in[trustee] += 1

    judge = 0
    for key in trust_out:
        if trust_out[key] == 0:
            judge = key

    if judge > 0 and trust_in[judge] == (n - 1):
        return judge
    else:
        return -1


def find_judge_alden(n, trust):
    people = []

    for i in range(1, n + 1):
        people.append(i)

    for el in trust:
        if el[0] in people:
            people.remove(el[0])

    if people:
        return people[0]

    else:
        return -1


def find_judge_alden_02(n, trust):
    people = [i for i in range(1, n + 1)]

    for el in trust:
        if people[el[0]] is not None:
            people[el[0]] = None
    for el in people:
        if el is not None:
            return el


def runner(func):
    print(f"{func.__name__}-----------")
    print(func(2, [[1, 2]]))  # 2
    print(func(2, []))  # -1
    print(func(3, [[1, 3], [2, 3]]))  # 3
    print(func(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))  # 3


runner(find_judge_beej)
runner(judge_trust)
runner(find_judge_alden)
# runner(find_judge_alden_02)
