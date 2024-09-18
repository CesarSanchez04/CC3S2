#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

// Esta es una implementación del algoritmo de Dijkstra para encontrar el camino más corto en un grafo dirigido

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

// se define las variables con sus respectivos valores
// las distancias se inicializan con valores infinitos 
// la lista visitado incializa todo en falso ya que al inicio del algoritmo ningun nodo fue visitado aun
// la lista previo inicia en -1 ya que no hay nodo previo al inicio
void init() {
	for (int i = 0; i < MAX; ++i) {
		distancia[i] = INF;
		visitado[i] = false;
		previo[i] = -1;
	}
}

// se define la función que realiza la minimización de las distancias
// esto logra que en el caso haya un camino aun mejor al conseguido se cambia el camino optimo
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

	// se crea una cola de prioridad y se encola el nodo inicial con distancia 0
	priority_queue<Nodo, vector<Nodo>, Compare> Q;
	distancia[inicial] = 0;
	Q.push(Nodo(inicial, 0));

	// mientras la cola de prioridad no ese vacia el bucle continua 
	while (!Q.empty()) {
		// se elige al primero de la cola de prioridad
		int actual = Q.top().first;
		// se borra al primero de la cola de prioridad luego de copiarlo a la variable actual
		Q.pop();

		// si el nodo ya ha sido visitado se sigue al siguiente nodo
		if (visitado[actual]) continue;
		visitado[actual] = true;
		
		// se itera sobre los nodos adyacentes al nodo actual y se minimiza la distancia si es necesario
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
	// se instancia las variables iniciales para el algoritmo
	// V = cantidad de nodos , E = cantidad de aristas , origen = nodo inicial , destino = nodo final, peso = distancia o peso a tratar entre los
	// nodos (origen y destino) , inicial = vertice donde se inicia el algoritmo
	int V, E, origen, destino, peso, inicial;
	
	cout << "\tBienvenido al programa de Grafos para hallar la distancia mas corta de un nodo o vertice al otro." << endl;
	cout << "\tIngrese la cantidad de nodos y arcos que contendra el grafo." << endl;
	cout << "\tIngrese el numero de nodos: ";
	cin >> V;
	cout << "\tIngrese el numero de arcos: ";
	cin >> E;
	
	// Se procede a solicitar las aristas en base a la cantidad de nodos y aristas elegidas por el usuario
	// Se añaden las aristas usando colas
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
