#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

#define MAX 10005
#define INF numeric_limits<int>::max()

typedef pair<int, int> Nodo;

struct Compare {
	bool operator()(const Nodo& a, const Nodo& b) {
		return a.second > b.second;
	}
};

vector<Nodo> ady[MAX];
int distancia[MAX];
int previo[MAX];
bool visitado[MAX];

void init() {
	for (int i = 0; i < MAX; ++i) {
		distancia[i] = INF;
		visitado[i] = false;
		previo[i] = -1;
	}
}

void minimizacion(int actual, int adyacente, int peso) {
	if (distancia[actual] + peso < distancia[adyacente]) {
		distancia[adyacente] = distancia[actual] + peso;
		previo[adyacente] = actual;
	}
}

void print(int destino) {
	if (previo[destino] != -1)
		print(previo[destino]);
	cout << destino << " ";
}

void dijkstra(int inicial) {
	init();
	priority_queue<Nodo, vector<Nodo>, Compare> Q;
	distancia[inicial] = 0;
	Q.push(Nodo(inicial, 0));
	
	while (!Q.empty()) {
		int actual = Q.top().first;
		Q.pop();
		
		if (visitado[actual]) continue;
		visitado[actual] = true;
		
		for (const auto& nodo : ady[actual]) {
			int adyacente = nodo.first;
			int peso = nodo.second;
			
			if (!visitado[adyacente]) {
				minimizacion(actual, adyacente, peso);
				Q.push(Nodo(adyacente, distancia[adyacente]));
			}
		}
	}
	
	cout << "\tDistancias mas cortas iniciando en vertice " << inicial << endl;
	for (int i = 1; i <= MAX; ++i) {
		if (distancia[i] != INF)
			cout << "\tVertice " << i << ", distancia mas corta = " << distancia[i] << endl;
	}
	
	cout << "\tPara hallar el camino mas corto del vertice de origen al vertice destino," << endl;
	cout << "\tIngrese el vertice destino: ";
	int destino;
	cin >> destino;
	print(destino);
	cout << endl;
}

int main() {
	int V, E, origen, destino, peso, inicial;
	
	cout << "\tBienvenido al programa de Grafos para hallar la distancia mas corta de un nodo o vertice al otro." << endl;
	cout << "\tIngrese la cantidad de nodos y arcos que contendra el grafo." << endl;
	cout << "\tIngrese el numero de nodos: ";
	cin >> V;
	cout << "\tIngrese el numero de arcos: ";
	cin >> E;
	
	cout << "\tIngresar el nodo o vertice de origen, su arista y la distancia o peso de un nodo a otro dejando un espacio entre cada numero." << endl;
	for (int i = 0; i < E; i++) {
		cin >> origen >> destino >> peso;
		ady[origen].push_back(Nodo(destino, peso));
	}
	
	cout << "\tIngrese el vertice inicial: ";
	cin >> inicial;
	
	dijkstra(inicial);
	
	return 0;
}
