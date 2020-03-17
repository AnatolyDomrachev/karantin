#include <stdio.h>
#include <iostream>

#pragma pack (push, 1)

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

using namespace std;

#pragma pack ( pop)

int main()
{
	struct BITMAPFILEHEADER h1;
	struct BITMAPINFO h2;

	FILE *f_in = fopen("cat.bmp","rb");
	fread(&h1, sizeof(h1), 1, f_in );
	fread(&h2, sizeof(h2), 1, f_in );
	
        cout << h1.bfSize << "  " << h2.biWidth << endl;

	fclose(f_in);
	
	return 0;
}