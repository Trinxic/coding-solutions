def fill_apartments(
    num_applicants: int,
    num_apartments: int,
    max_difference: int,
    applicants: list[int],
    apartments: list[int],
) -> int:
    # priority = { applicant: [(ranked) desired apartments] }
    priority = [dict(key) for key in applicants]
    for applicant in applicants:
        for apartment in apartments:
            if (
                applicant < apartment + max_difference
                and applicant > apartment - max_difference
            ):
                priority[applicant].append(apartment)


def main():
    info = []
    for i, x in enumerate(input().split()):
        info[i] = x
    print(
        info[0],
        info[1],
        info[2],
        [int(n) for n in input().split()],
        [int(n) for n in input().split()],
    )


if __name__ == "__main__":
    main()


# is 13 5 within 10?
# 13 < 10+5 or 13 > 10-5
