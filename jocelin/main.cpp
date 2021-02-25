#include "main.h"


#define IN_DIR "/Users/mac/CLionProjects/hashcode2021/jocelin/inputs/"
#define OUT_DIR "/Users/mac/CLionProjects/hashcode2021/jocelin/outputs/"
#define MAX_S 100001
#define MAX_V 1001

string pb = "a";
int D, I, S, V, F;
string streetNames[MAX_S];
map<string, int> streetIntValue;
int streetStarts[MAX_S];
int streetEnds[MAX_S];
int streetLengths[MAX_S];
int carTimeSpendInStreet[MAX_S];
int carsTotalTime[MAX_V];
map<int, vector<int>> carInStreet;
map<int, vector<int>> carPaths;
map<int, vector<int>> streetEnterIntersection;
map<int, vector<int>> streetOutIntersection;
vector<int> cars;
vector<int> streets;
int sheduled[MAX_S];

void readInput() {
    string in_file = IN_DIR + pb + ".txt";
    freopen(in_file.c_str(), "r", stdin);
    cin >> D >> I >> S >> V >> F;
    for (int i = 0; i < S; ++i) {
        int b, e, l;
        string street_name;
        cin >> b >> e >> street_name >> l;
        streetStarts[i] = b;
        streetEnds[i] = e;
        streetLengths[i] = l;
        streetNames[i] = street_name;
        streetIntValue[street_name] = i;
        streetEnterIntersection[e].push_back(i);
        streetOutIntersection[b].push_back(i);
    }
    for (int i = 0; i < V; ++i) {
        int p, totalTime = 0;
        cin >> p;
        for (int j = 0; j < p; ++j) {
            string street;
            cin >> street;
            carPaths[i].push_back(streetIntValue[street]);
            totalTime += streetLengths[streetIntValue[street]];
            if (j == 0)
                carInStreet[streetIntValue[street]].push_back(i);
        }
        carsTotalTime[i] = totalTime;
    }
}

void runCar(int car) {
    vector<int> paths = carPaths[car];
    for (int i = 0; i < paths.size(); ++i) {

    }
}

void solve() {
    memset(sheduled, -1, sizeof sheduled);
//    for (int i = 0; i < V; ++i) cars.push_back(i);
//    sort(cars.begin(), cars.end(), [](int c1, int c2) { return carsTotalTime[c1] < carsTotalTime[c2]; });
    for (int i = 0; i < I; ++i) {
        vector<int> streets = streetEnterIntersection[i];
        sort(streets.begin(), streets.end(),
             [](int s1, int s2) { return carInStreet[s1].size() > carInStreet[s2].size(); });
        int lt = D;
        for (int j = 0; j < streets.size(); ++j) {
            //sheduled[streets[i]] =
        }
    }
}

void output() {
    string out_file = OUT_DIR + pb + ".txt";
    FILE *fp = fopen(out_file.c_str(), "w");
    fprintf(fp, "%d\n", I);
    for (int i = 0; i < I; ++i) {
        fprintf(fp, "%d\n%d\n", i);
        vector<int> streets = streetEnterIntersection[i];
        sort(streets.begin(), streets.end(),
             [](int s1, int s2) { return carInStreet[s1].size() > carInStreet[s2].size(); });

    }
}

int main() {
    readInput();
    solve();
    output();

    return 0;
}
