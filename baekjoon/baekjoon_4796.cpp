#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <string>


using namespace std;

int main() {
	int a, b, c;
	vector<int> P,L,V;
	
	while (true) {
		
		cin >> a >> b >> c;
		L.push_back(a);
		P.push_back(b);
		V.push_back(c);
		if (a == 0) {
			break;
		}
	}
	int i=0;
	while (i != V.size()-1) {
		int sum = 0;
		int n = V[i];
		while (true) {
			
			
			if (n - P[i] >= 0) {
				n = n - P[i];
				sum += L[i];
			}
			else {
				if (n > L[i]) {
					sum += L[i];
					i++;
					printf("Case %d: %d\n", i, sum);
					break;
				}
				else {
					sum += n;
					i++;
					printf("Case %d: %d\n", i, sum);
					break;
				}
			}
			
			
		}
		
	}
	system("pause");
	return 0;
}
