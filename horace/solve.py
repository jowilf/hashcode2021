

class Street:

    def __init__(self, start, end, name, duration):
        self.start = start
        self.end = end
        self.name = name
        self.duration = duration
        # shceduled time
        self.t_time = 0
        # to create position
        self.weight = 0
        self.time = 1
        self.car_len = 0


class Car:

    def __init__(self, _id, streets_len):
        self.id = _id
        self.size = streets_len
        self.streets = []

    def add_street(self, street):
        self.streets.append(street)


class Intersection:

    def __init__(self, number):
        self.number = number
        self.streets = []
        self.streets_dict = {}

    def add_street(self, street):
        street.weight = 1
        self.streets.append(street)
        self.streets_dict[street.name] = street



class Problem:

    def __init__(self, input_path):
        self.input_path = input_path
        self.streets_dict = {}
        self.cars_dict = {}
        self.intersections_dict = {}
        self.streets = []
        self.cars = []
        self.intersections = []


        with open(input_path) as f:
            duration, inter_le, street_len, cars_len, bonus = list(
                map(lambda x: int(x), f.readline().strip().split(' '))
            )
            # print(duration, inter_le, street_len, cars_len, bonus)
            self.duration = duration
            self.inter_le = inter_le
            self.street_len = street_len
            self.cars_len = cars_len
            self.bonus = bonus
            
            for i in range(self.street_len):
                line_items = f.readline().strip().split(' ')
                street = Street(
                    int(line_items[0]),
                    int(line_items[1]),
                    line_items[2],
                    int(line_items[3])
                )
                self.streets.append(street)
                self.streets_dict[street.name] = street

                if street.end not in self.intersections_dict.keys():
                    new_intersection = Intersection(street.end)
                    new_intersection.add_street(street)
                    self.intersections.append(new_intersection)
                    self.intersections_dict[
                        new_intersection.number
                    ] = new_intersection
                else:
                    intersection = self.intersections_dict[street.end]
                    intersection.add_street(street)


            for i in range(self.cars_len):
                line_items = f.readline().strip().split(' ')
                car = Car(i, int(line_items[0]))
                for street_name in line_items[1:]:
                    street = self.streets_dict[street_name]
                    car.add_street(street)
                    street.weight += car.size
                    street.car_len += 1
                self.streets_dict[line_items[1]].time += 1
                
                self.cars_dict[i] = car
                self.cars.append(car)
            # print(self.cars[0].streets_names)
    
    def solve(self):
        out_str = ''
        schedule_str = ''
        schedule_count = 0
        selected_intersections = []
        for intersection in self.intersections:
            if len(intersection.streets):
                schedule_count += 1
                selected_intersections.append(intersection)
                schedule_str += str(intersection.number) + '\n'
                streets_count = 0
                streets_str = ''
                intersection.streets.sort(key=lambda x: x.weight, reverse=True)
                intersection.streets.sort(key=lambda x: x.time, reverse=True)
                for i in range(len(intersection.streets)):
                    street = intersection.streets[i]
                    if True: # street.car_len:
                        # time = int(street.duration/((i+2)*2))
                        car_len = street.car_len
                        if not car_len:
                            car_len = 1
                        # time = int(car_len/2) + int(street.duration/10)
                        time = int((street.time + street.duration + car_len)/5)
                        # time = int((street.duration/car_len)/10)
                        if time == 0:
                            time = 1
                        streets_str += street.name + ' ' + str(time) + '\n'
                        streets_count += 1
                schedule_str += str(streets_count) + '\n' + streets_str

        out_str = str(schedule_count) + '\n' + schedule_str

        with open(self.input_path + '.out', 'w') as f:
            f.write(out_str)
        
        return selected_intersections
    
    def simulate(self, solutionselected_intersections):
        pass
        
        



if __name__  == "__main__":
    import sys
    problem = Problem(sys.argv[1])
    problem.solve()
