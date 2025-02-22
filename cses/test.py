def main():
    lst = [1, 2, 2, 3]
    test = [{key: []} for key in lst]
    print(test)
    test[1][2] = 3
    print(test)


if __name__ == "__main__":
    main()
