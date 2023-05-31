#include <bits/stdc++.h>
using namespace std;

#define MAXLIST 100
typedef struct Sinhvien
{
    char HoTen[MAXLIST];
    char MSSV[MAXLIST];
} Sinhvien;

typedef struct danhsachdac
{
    Sinhvien dssv[MAXLIST];
    int num;
} List;

// Khoi tao
void Init(List &plist)
{
    plist.num = 0;
}
// Xac dinh so nut cua danh sách
int ListSize(List plist)
{
    return plist.num;
}
// Kiem tra danh sách rong
int IsEmpty(List plist)
{
    return (plist.num == 0);
}
// Kiem tra danh sách day
int IsFull(List plist)
{
    return (plist.num == MAXLIST);
}

// Nhap thong tin sinh vien
void Nhapsv(Sinhvien &sv)
{
    int i;
    printf("\n\t Nhap ho ten sinh vien: ");
    fflush(stdin);
    fgets(sv.HoTen, MAXLIST, stdin);
    printf("\t Nhap MSSV: ");
    fflush(stdin);
    fgets(sv.MSSV, MAXLIST, stdin);
}

// Nhap danh sach sinh vien
void Nhapds(List &plist, Sinhvien &sv)
{
    int i;
    do
    {
        printf("\n\t Nhap so luong sinh vien: ");
        scanf("%d", &plist.num);
    } while (plist.num < 0);
    if (IsFull(plist))
    {
        printf("\n ==> Danh sach bi day!");
        return;
    }
    else
    {
        for (i = 0; i < plist.num; i++)
        {
            printf("\n\t -- Nhap thong tin sinh vien thu %d -- ", i + 1);
            Nhapsv(plist.dssv[i]);
        }
    }
}

// Xuat sinh vien
void Xuatsv(Sinhvien sv)
{
    int i;
    printf("\n\t Ho ten: %s", sv.HoTen);
    printf("\n\t Ma so sinh vien: %s\n", sv.MSSV);
}

// Xuat danh sách
void ShowList(List plist)
{
    if (plist.num == 0)
    {
        printf("\n\t ==> Danh sach khong co sinh vien!");
        return;
    }
    else
    {
        for (int i = 0; i < plist.num; i++)
        {
            printf("\n\t -- Thong tin sinh vien thu: %d --", i + 1);
            Xuatsv(plist.dssv[i]);
        }
    }
}

// Tim kiem sinh vien
int Find(List plist, char x[MAXLIST])
{
    Sinhvien sv;

    for (int i = 0; i < plist.num; i++)
    {

        if (strcmp(plist.dssv[i].MSSV, x) == 0)
        {
            //
            printf("\n\t Sinh vien can tim có MSSV: %s", x);
            printf('\n\t Ho ten sinh vien la: %s',plist.dssv[i].HoTen);
            return i;
        }
    }
    printf("\n\t Khong tim thay sinh vien co MSSV la %s", x);
    return -1; // tuc la khong tim thay sinh vien
}

// Xoa toan bo danh sach SV
void ClearList(List &plist)
{
    plist.num = 0;
}

// Hàm chính
int main(int argc, char **argv)
{

    List plist;
    Sinhvien sv;
    Init(plist);

    int chon, x, i, k;
    do
    {
        // Nhap chon lua cua nguoi dùng
        printf("\n\t------------------ CHUONG TRINH QUAN LY SINH VIEN DANH SACH DAC --------------------");
        printf("\n\t 1: Nhap danh sach sinh vien\n");
        printf("\n\t 2: Xuat danh sach sinh vien\n");
        printf("\n\t 3: Them mot sinh vien vao danh sach\n");
        printf("\n\t 4: Xoa mot sinh vien khoi danh sach\n");
        printf("\n\t 5: Hieu chinh thong tin sinh vien\n");
        printf("\n\t 6: Sap xep danh sach sinh vien tang theo ma sinh vien\n");
        printf("\n\t 7: Tim kiem sinh vien theo ma sinh vien\n");
        printf("\n\t 8: Xoa toan bo danh sach sinh vien\n");
        printf("\t 0: Thoat (Bam phim bat ky de tiep tuc)\n");
        printf("\n\t Hay chon chuc nang: ");
        scanf("%d", &chon);

        // Thuc hien công viec cho lua chon tuong ung
        switch (chon)
        {
        case 1: // Nhap danh sach sinh vien
            Nhapds(plist, sv);
            printf("\n");
            getchar();
            system("cls");
            break;
        case 2: // xuat danh sach sinh vien
            ShowList(plist);
            printf("\n");
            getchar();
            system("cls");
            break;

        case 3: // tim kiem sinh vien

            printf("\n\t-----Tim kiem sinh vien-----\n");
            char mssv[MAXLIST];
            printf("\tNhap MSSV sinh vien can tim: ");
            fflush(stdin);
            fgets(mssv, MAXLIST, stdin);
            int index = Find(plist, mssv);
            if (index == -1)
            {
                printf("\tKhong tim thay sinh vien co MSSV la %s\n", mssv);
            }
            else
            {
                printf("\tSinh vien co MSSV la %s la: \n", mssv);
                Xuatsv(plist.dssv[index]);
            }
            getchar();
            system("cls");
            break;

        case 4: // Xoa danh sach sinh vien
            printf("\n\t-----Xoa danh sach sinh vien-----\n");
            ClearList(plist);
            printf("\tDa xoa toan bo danh sach sinh vien\n");
            getchar();
            system("cls");
            break;

        case 5:
            printf("\n\t Ban da chon thoat chuong trinh.Hen gap lai!");
            break;
        default:
            chon = 0;
            break;
        }

        // getchar();

    } while (chon != 0);
    return 0;
}