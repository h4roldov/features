import argparse
import math
import statistics


def run(args):
    input_dataset = open(args.input_file, "r")
    output_file = open(args.output_file, "w")
    eje_x = []
    eje_y = []
    eje_z = []
    # lines_to_evaluate = args.lines
    lines = input_dataset.readlines()
    number_of_lines = len(lines)
    print(number_of_lines)

    for line in lines[4:]:
        line = line.split(",", 7)[:4]
        eje_x.append(float(line[1]))
        eje_y.append(float(line[2]))
        eje_z.append(float(line[3]))

    # for element in eje_x:
    #     print(element)
    listaz = [7, 7, 31, 31, 47, 75, 87, 115, 116, 119, 119, 155, 177]
    # print(IQR(listaz))
    # print(variance(listaz))
    print(skewness(listaz))
    print(std(listaz))
    print(mean_(listaz))
    print(variance(listaz))

    # Results string
    results = (" RMS: " +
               "\n x = " + str(RMS(eje_x)) +
               "\n y = " + str(RMS(eje_y)) +
               "\n z = " + str(RMS(eje_z)) +
               "\n Mean : " +
               "\n x = " + str(mean_(eje_x)) +
               "\n y = " + str(mean_(eje_y)) +
               "\n z = " + str(mean_(eje_z)) +
               "\n Max : " +
               "\n x = " + str(max(eje_x)) +
               "\n y = " + str(max(eje_y)) +
               "\n z = " + str(max(eje_z)) +
               "\n Min : " +
               "\n x = " + str(min(eje_x)) +
               "\n y = " + str(min(eje_y)) +
               "\n z = " + str(min(eje_z)) +
               "\n IQR : " +
               "\n x = " + str(IQR(eje_x)) +
               "\n y = " + str(IQR(eje_y)) +
               "\n z = " + str(IQR(eje_z)) +
               "\n Variance : " +
               "\n x = " + str(variance(eje_x)) +
               "\n y = " + str(variance(eje_y)) +
               "\n z = " + str(variance(eje_z)) +
               "\n Standard deviation : " +
               "\n x = " + str(std(eje_x)) +
               "\n y = " + str(std(eje_y)) +
               "\n z = " + str(std(eje_z)))

    # Adds the results string into the results.txt file
    output_file.write(results)
    output_file.close()
    print(statistics.mean(eje_x))

 # Mean


def mean_(list_):
    return sum(list_)/len(list_)

# Root mean square


def RMS(list_):
    mean_square = 0
    for element in list_:
        mean_square = mean_square + (float(element)*float(element))
    mean_square = mean_square/len(list_)

    return math.sqrt(mean_square)

# Interquartile range, using wikipedia formula (wolfram also)


def IQR(list_):
    iqr = 0
    list_.sort()
    length = len(list_)
    mod = length % 4
    n = (length - mod) / 4
    n = int(n)
    if(mod == 1):
        iqr = (0.75 * list_[3*n] + 0.25 * list_[3*n+1]) - \
            (0.25 * list_[n-1] + 0.75 * list_[n])
    elif (mod == 3):
        iqr = (0.25 * list_[3*n+1] + 0.75 * list_[3*n+2]) - \
            (0.75*list_[n] + 0.25 * list_[n+1])
    elif (length % 2 == 0):
        if(length/4 % 2 == 0):
            iqr = (list_[3*int(length/4)] + list_[3*int(length/4)-1]) / \
                2 - (list_[int(length/4)] + list_[int(length/4)-1])/2
        else:
            iqr = list_[3*int(math.ceil(length/4))-2] - \
                list_[int(math.ceil(length/4))-1]

    return iqr

# Variance


def variance(list_):
    # mean = sum(list_)/len(list_)
    mean = mean_(list_)
    return sum((xi - mean)**2 for xi in list_)/(len(list_)-1)

# Standard deviation


def std(list_):
    std = math.sqrt(variance(list_))
    return std

# skewness


def skewness(list_):
    mean = mean_(list_)
    return (sum((xi - mean)**3 for xi in list_)/(len(list_)-1))/(std(list_)**3)

    # argparse


def main():
    parser = argparse.ArgumentParser(
        description="Calculate features from selected dataset")
    parser.add_argument("-input", help="Dataset file",
                        dest="input_file", type=str, required=True)
    parser.add_argument("-output", help="Features values file",
                        dest="output_file", type=str, required=False, default="results.txt")
    parser.add_argument("-lines", help="Define the number of lines to calculate features",
                        dest="lines", type=check_positive, required=False, default=-1)

    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

# check if the amount of lines is positive


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            "%s is an invalid positive int value" % value)
    return ivalue


if __name__ == "__main__":
    main()
