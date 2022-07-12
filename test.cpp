
#include <iostream>
#include <cstring>
using namespace std;

class SinhVien
{
private:
    int id;
    string hoten;
    float diemTB;
    friend class DSSV;
public:
    void Nhap(){
        cout << "Nhap ho ten: "; fflush(stdin); getline(cin, this->hoten);
        cout << "Nhap id: "; cin >> id;
        cout << "Nhap diemTb: "; cin >> diemTB;  
    }
    void Xuat(){
        cout << "ID: " << this->id << endl;
        cout << "Ho va ten: " << this->hoten << endl;
        cout << "Diem TB: " << this->diemTB << endl; 
    }
    float getDiem(){
        return this->diemTB;
    }
};

class DSSV
{
private:
    int n;
    SinhVien s[];

public:
    void Input();
    void Output();
    float maxDiem();
    void Sapxep(); // sap xep theo chieu diem trung binh gian dan
                   // neu co cung diem tb thi sap xep theo chieu tang dan cua ho ten
};

void DSSV::Input()
{

    cout << "Nhap so luong sinh vien: ";
    cin >> this->n;
    for (int i = 0; i < n; i++)
    {
        cout << "Nhap sinh vien thu: " << i + 1 << endl;
        s[i].Nhap();
    }
}
void DSSV::Output()
{

    for (int i = 0; i < n; i++)
    {
        s[i].Xuat();
    }
}

int main(int argc, char const *argv[])
{
    DSSV l;
    l.Input();
    l.Output();
    return 0;
}