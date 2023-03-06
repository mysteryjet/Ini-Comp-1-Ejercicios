#include <iostream>

using namespace std;

int main()
{
    float num1, num2, resultado;
    int opcion;

    cout << "Ingrese el primer número: ";
    cin >> num1;

    cout << "Ingrese el segundo número: ";
    cin >> num2;

    cout << "Ingrese la operación que desea realizar:" << endl;
    cout << "1. Suma" << endl;
    cout << "2. Resta" << endl;
    cout << "3. Multiplicación" << endl;
    cout << "4. División" << endl;
    cin >> opcion;

    switch(opcion)
    {
        case 1:
            resultado = num1 + num2;
            cout << "El resultado de la suma es: " << resultado;
            break;
        case 2:
            resultado = num1 - num2;
            cout << "El resultado de la resta es: " << resultado;
            break;
        case 3:
            resultado = num1 * num2;
            cout << "El resultado de la multiplicación es: " << resultado;
            break;
        case 4:
            if(num2 == 0)
            {
                cout << "Error: no es posible dividir entre cero";
            }
            else
            {
                resultado = num1 / num2;
                cout << "El resultado de la división es: " << resultado;
            }
            break;
        default:
            cout << "Error: opción inválida";
            break;
    }

    return 0;
}
