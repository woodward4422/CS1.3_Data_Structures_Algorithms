from binarytree import BinarySearchTree
import sys
import os


def get_phone_list(filename):
    with open(filename) as stream:
        phone_list = stream.read().splitlines()
    return phone_list


def get_route_dict(filename):
    routes = {}
    with open(filename) as file:
        for line in file:
            route, value = line.strip().split(',')

            routes[route] = float(value)
        return routes


def get_phone_numbers_list(filename):
    phone_numbers = []
    with open(filename) as numbers_file:
        for phone_number in numbers_file:
            phone_number = phone_number.strip()
            phone_numbers.append(phone_number)
    return phone_numbers


def challenge_one(input_number, route_file):
    if len(input_number) != 12:  # Catches the case if the phone number is not formatted properly
        return None
    routes = get_route_dict(route_file)
    # Iterate through the input number backwards while checking to see if the prefix up until the current index is in the dictionary
    for i in range(len(input_number), 0, -1):
        # This will give us the prefix all the way up to i and see if it is in the routes dictionary
        number_prefix = input_number[:i]
        if number_prefix in routes:
            return routes[number_prefix]


def challenge_two(input_numbers_file, route_file):
    call_values = []
    routes = get_route_dict(route_file)
    phone_numbers = get_phone_list(input_numbers_file)
    phone_numbers.pop()
    # print("Phone Numbers: {}".format(phone_numbers))
    for phone_number in phone_numbers:
        print(phone_number)
        found = False
        for i in range(len(phone_number), 0, -1):
            number_prefix = phone_number[:i]
            if number_prefix in routes:
                call_values.append((phone_number, routes[number_prefix]))
                found = True
                break
        if not found:
            call_values.append((phone_number, 0))
    print("Output: {}".format(call_values))
    return call_values


def create_lowest_cost_dict(routes_files: list):
    routes = {}
    for route_file_name in routes_files:
        with open(route_file_name) as routes_file:
            for line in routes_file:
                route, value = line.strip().split(',')
                if float(value) <= routes.get(route, float(value)):
                    routes[route] = float(value)
    return routes


def challenge_three(input_numbers_file: str, routes_files: list):
    routes = create_lowest_cost_dict(routes_files)
    phone_numbers = get_phone_numbers_list(input_numbers_file)
    call_values = []
    print("Cheap Routes: {}".format(routes))
    print("Phone Numbers: {}".format(phone_numbers))
    for phone_number in phone_numbers:
        found = False
        for i in range(len(phone_number), 0, -1):
            number_prefix = phone_number[:i]
            if number_prefix in routes:
                call_values.append((phone_number, routes[number_prefix]))
                found = True
                break
        if not found:
            call_values.append((phone_number, 0))
    return call_values
