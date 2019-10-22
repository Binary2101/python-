#include <stdio.h>
#include <stdlib.h>
int a[500];
int b[40][40][40][40];
int sq[5];
int main()
{
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &a[i]);
	}
	for (int i = 1; i <= m; i++)
	{
		int tmp;
		scanf("%d", &tmp);
		sq[tmp]++;
	}
	for (int i = 0; i <= sq[1]; i++)
	{
		for (int j = 0; j <= sq[2]; j++)
		{
			for (int k = 0; k <= sq[3]; k++)
			{
				for (int l = 0; l <= sq[4]; l++)
				{
					int tmp = 0;
					int val = i * 1 + j * 2 + k * 3 + l * 4 + 1;
					if (i) tmp = max(tmp, b[i - 1][j][k][l]);
					if (j) tmp = max(tmp, b[i][j - 1][k][l]);
					if (k) tmp = max(tmp, b[i][j][k - 1][l]);
					if (l) tmp = max(tmp, b[i][j][k][l - 1]);
					b[i][j][k][l] = tmp + a[val];

				}
			}
		}
	}
	printf("%d\n", b[sq[1]][sq[2]][sq[3]][sq[4]]);
	return 0;
}