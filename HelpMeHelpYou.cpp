#include<iostream>
#include<string>
#include<unistd.h>
#define max 10000
using namespace std;

struct Article
{
    /* data */
    string name;
    int num;
    string address;
};
struct Articlebooks
{
    Article articleArray[max];
    int size;
    
};
void showMenu()
{
    cout << "***** 1、添加物品 *****" << endl;
    cout << "***** 2、显示物品 *****" << endl;
    cout << "***** 3、删除物品 *****" << endl;
    cout << "***** 4、查找物品 *****" << endl;
    cout << "***** 0、退出系统 *****" << endl;
}

//add person
void addArticle(Articlebooks * abs)
{
    if(abs->size == max)
    {
        cout << "FULL OF BOOK! "<< endl;
        return;
    }
    else
    {
        string name;
        cout << "Name: "<< endl;
        cin >> name;
        abs->articleArray[abs->size].name = name;
        cout << "Num: "<< endl;
        int num = 0; 
        while(true)
        {
            cin >> num;
            if(num > 0)
            {
                abs->articleArray[abs->size].num = num;
                break;
            }
            else
            {
                cout<< "Wrong!" << endl;
            }
        }

        string address;
        cout << "Address: (XXX号XXX室)"<< endl;
        cin >> address;
        abs->articleArray[abs->size].address = address;

        abs->size++;
        cout << "Success!" << endl;
    }
}

void showArticle(Articlebooks * abs)
{
    if(abs->size == 0)
    {
        cout << "Empty" << endl;
    }
    else{
        for (int i = 0 ;i< abs->size;i++)
        {
            cout << "Name:"<<abs->articleArray[i].name << "\t";
            cout << "Address:"<<abs->articleArray[i].address << "\t";
            cout << "Num:"<<(abs->articleArray[i].num)<< endl;
        }
    }
}
int isExist(Articlebooks * abs, string name)
{
    for( int i = 0; i < abs->size; i++)
    {
        if (abs->articleArray[i].name == name)
        {
            return i;
        }
    }
    return -1;
}

void deleteArticle(Articlebooks * abs)
{
    cout << "请输入删除物品的名称: "<< endl;
    string name;
    cin >> name;
    int ret = isExist(abs,name);

    if (ret == -1){
        cout << "找不到！ "<< endl;
    }
    else{
        cout << "找到啦! "<< endl;
        for (int i = ret;i < abs->size;i++){
            abs->articleArray[i] = abs->articleArray[i+1];
        }
        abs->size--;
        cout << "删除成功！ "<< endl;

    }
}
int main()
{
    Articlebooks abs;
    abs.size = 0;

    int select = 0;
    while (true)
    {
        showMenu();
        cin >> select;
        switch (select)
        {
            case 1/* constant-expression */:
                /* code */
                addArticle(&abs);
                break;
            case 2/* constant-expression */:
                /* code */
                showArticle(&abs);
                break;
            case 3 /*constant-expression */:
                /* code */
                deleteArticle(&abs);
                break; 
            case 4/* constant-expression */:
            {    /* code */
                cout << "请输入搜索物品的名称: "<< endl;
                string name;
                cin >> name;
                if (isExist(&abs, name)== -1)
                {
                    cout << "找不到！ "<< endl;
                }
                else
                {
                    cout << "找到啦! 物品在第"<<isExist(&abs, name)<<"位"<< endl; 
                }    
                break;   
            } 
            case 0/* constant-expression */:
                /* code */
                cout << "欢迎下次使用" << endl;
                break;
            default:
                break;
        }
    }
    
    return 0;
}