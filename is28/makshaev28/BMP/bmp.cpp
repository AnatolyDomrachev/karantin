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

#pragma pack ( pop)

int main()
{
	struct BITMAPFILEHEADER h1;
	struct BITMAPINFO h2;

	FILE *del = fopen("del.bmp","rb");
	fread(&h1, sizeof(h1), 1, del);
	fread(&h2, sizeof(h2), 1, del );

	fclose(del);
	
	cout << h2.biWidth<<" "<<h2.biHeight<<" "<<h1.bfSize<<endl;

	return 0;
	
	
}

