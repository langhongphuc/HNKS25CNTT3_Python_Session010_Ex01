cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print('''
=============================================          
       SHOPEE CART MANAGEMENT SYSTEM
=============================================
1. Xem chi tiêt giỏ hàng & Tính tổng tiên
2. Thêm sản phẩm mới / Cộng dôn sô lượng
3. Cập nhật sô lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
=============================================
''')
    
    choice = input('Mời bạn chọn chức năng (1-5): ')

    if choice == '1':
        total_price = 0
        for i, item in enumerate(cart_items):
            total_price += item[2] * item[3]
        print('TỔNG TIỀN THANH TOÁN: ', total_price)

    elif choice == '2':
        product_id = input('Nhập mã sản phẩm: ')
        found = False
        for i, item in enumerate(cart_items):
            if product_id == item[0]:
                found = True
                quantity = int(input('Nhập số lượng: '))
                item[2] += quantity
                break
        
        if found == False:
            product_name = input('Nhập tên sản phẩm: ')
            quantity = int(input('Nhập số lượng sản phẩm'))
            price = float(input('Nhập đơn giá: '))
            cart_items.append(product_name, quantity, price)

    elif choice == '3':
        product_id = input("Nhập mã sản phẩm cần cập nhật: ")
        new_quantity = int(input("Nhap so luong moi: "))

        if new_quantity <= 0:
            print("Số lượng phải lớn hơn 0")

        else:
            found = False
            for item in cart_items:
                if item[0] == product_id:
                    item[2] = new_quantity

                    found = True

                    print("Cập nhật thành công !")

            if found == False:

                print("Ma san pham khong ton tai trong gio hang.")
                    
    elif choice == '4':
        product_id = input("Nhập mã sản phẩm cần xóa: ")

        found = False

        for item in cart_items:
            if item[0] == product_id:
                cart_items.remove(item)

                found = True

                print("Đã xóa thành công !")
                break

        if found == False:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                
    elif choice == '5':
        print('Thoát chương trình !!!')
        break

    else:
        print('Lựa chọn không hợp lệ, vui lòng nhập từ 1-5')