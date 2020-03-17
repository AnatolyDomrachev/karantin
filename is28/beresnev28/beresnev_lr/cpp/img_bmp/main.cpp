#include <iostream>
#include <stdio.h>
#pragma pack (push, 1)

using namespace std;

struct BITMAPFILEHEADER
{
	char bfType[2];
	int bfSize;
	char bfReserved1[2];
	char bfReserved2[2];
	int bfOffBits;
};

struct BITMAPINFO
{
	int biSize;
	int biWidth;
	int biHeight;
	char biPlanes[2];
	char biBitCount[2];
	int biCompression;
	int biSizeImage;
	int biXPelsPerMeter;
	int biYPelsPerMeter;
	int biClrUsed;
	int biClrImportant;
};

#pragma pack ( pop)

int main()
{
	struct BITMAPFILEHEADER h1;
	struct BITMAPINFO h2;

	FILE *f_in = fopen("img.bmp","rb");
	fread(&h1, sizeof(h1), 1, f_in );
	fread(&h2, sizeof(h2), 1, f_in );


	fclose(f_in);

	cout << h2.biWidth << " " << h2.biHeight << " " << h1.bfSize << endl;

	return 0;
}
