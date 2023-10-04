#include <stdio.h>
#include <string.h>

struct Items
{
    char Name[100];
    int quantity;
};

struct Player
{
    char name[30];
    int levels;
    int count_Items; // Length of items
    int Maximum_inventory_size;
    struct Items items[100];
};

void Initialize_Player(struct Player *Ply, char name[30])
{
    Ply->count_Items = 0;
    Ply->levels = 1;
    Ply->Maximum_inventory_size = 10;

    strcpy(Ply->name, name);
}

int Add_Item_Inventory(struct Player *player)
{
    printf("\n");
    printf("Enter item name : ");
    getchar();
    fgets(player->items[player->count_Items].Name, 100, stdin);

    printf("Enter item quantity : ");
    scanf("%d", &player->items[player->count_Items].quantity);
    printf("\n");

    player->count_Items++;
}

int Remove_Item_From_Inventory(struct Player *player)
{
    char name_remove[30];
    char name[30];

    printf("Enter name : ");

    getchar();
    fgets(name_remove, 30, stdin);
    for (int i = 0; i < player->count_Items; i++)
    {
        if (strcmp(name_remove, player->items[i].Name) == 0)
        {
            strcpy(player->items[i].Name, name);
            player->items[i].quantity = 0;

            player->count_Items--;
        }
    }
}

int Display_Inventory(struct Player *player)
{
    printf("\n");
    for (int i = 0; i <= player->count_Items; i++)
    {
        if (player->items[i].quantity != 0)
        {
            printf("%s", player->items[i].Name);
            printf("%d\n", player->items[i].quantity);
        }
    }
    printf("\n");
}

int Upgrade_Inventory(struct Player *player)
{
    int upgrade;
    char name[30];

    printf("Enter name that quantity you have to Upgrade : ");
    getchar();
    fgets(name, 30, stdin);

    printf("Enter Upgrade : ");
    scanf("%d", &upgrade);

    for (int i = 0; i < player->count_Items; i++)
    {
        if (strcmp(name, player->items[i].Name) == 0)
        {
            player->items[i].quantity += upgrade;
        }
    }
}

int Trade_Items(struct Player *Player_A, struct Player *Player_B)
{
    char name1[100];
    char name2[100];
    char temp_name[100];
    int temp_quantity = 0;

    printf("\n");

    printf("Enter Player A item name : ");
    getchar();
    fgets(name1, 100, stdin);

    printf("Enter player B item name : ");
    fgets(name2, 100, stdin);
    printf("\n");

    for (int j = 0; j < Player_A->count_Items; j++)
    {
        if (strcmp(Player_A->items[j].Name, name1) == 0)
        {
            for (int k = 0; k < Player_B->count_Items; k++)
            {
                if (strcmp(Player_B->items[k].Name, name2) == 0)
                {
                    strcpy(temp_name, Player_A->items[j].Name);
                    strcpy(Player_A->items[j].Name, Player_B->items[k].Name);
                    strcpy(Player_B->items[k].Name, temp_name);

                    temp_quantity = Player_A->items[j].quantity;
                    Player_A->items[j].quantity = Player_B->items[k].quantity;
                    Player_B->items[k].quantity = temp_quantity;
                    break;
                }
            }
        }
        break;
    }
}

int main()
{
    struct Player Player_A;
    struct Player Player_B;

    Initialize_Player(&Player_A, "Player_A");
    Initialize_Player(&Player_B, "Player_B");

    int menu;

    printf("In menu which one you have to do, If don't enter '0'.\n");
    printf("1. Add Item To Inventory\n");
    printf("2. Remove Item From Inventory\n");
    printf("3. Display Inventory\n");
    printf("4. Upgrade Inventory\n");
    printf("5. Trade Items\n");
    printf("\n");

    printf("Enter number in menu : ");
    scanf("%d", &menu);

    while (menu != 0)
    {
        if (menu == 1)
        {
            char player;

            printf("Enter player name : ");

            getchar();
            scanf("%c", &player);

            if (player == 'A')
            {
                Add_Item_Inventory(&Player_A);
            }
            else if (player == 'B')
            {
                Add_Item_Inventory(&Player_B);
            }
            else
            {
                printf("Invalid name\n");
            }
        }
        else if (menu == 2)
        {
            char Remove;

            printf("Enter player name : ");

            getchar();
            scanf("%c", &Remove);

            if (Remove == 'A')
            {
                Remove_Item_From_Inventory(&Player_A);
            }
            else if (Remove == 'B')
            {
                Remove_Item_From_Inventory(&Player_B);
            }
            else
            {
                printf("Invalid name\n");
            }
        }
        else if (menu == 3)
        {
            char Display;

            printf("Enter player name : ");

            getchar();
            scanf("%c", &Display);

            if (Display == 'A')
            {
                Display_Inventory(&Player_A);
            }
            else if (Display == 'B')
            {
                Display_Inventory(&Player_B);
            }
        }
        else if (menu == 4)
        {
            char Upgrade;

            printf("Enter player name : ");

            getchar();
            scanf("%c", &Upgrade);

            if (Upgrade == 'A')
            {
                Upgrade_Inventory(&Player_A);
            }
            else if (Upgrade == 'B')
            {
                Upgrade_Inventory(&Player_B);
            }
        }
        else if (menu == 5)
        {
            Trade_Items(&Player_A, &Player_B);
        }
        printf("Enter number in menu : ");
        scanf("%d", &menu);
    }
    return 0;
}