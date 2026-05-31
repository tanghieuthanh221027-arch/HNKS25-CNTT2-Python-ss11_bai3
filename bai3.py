product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    choice = input("""
===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình

Nhập lựa chọn: """)

    if not choice.isdigit() or int(choice) not in range(1, 6):
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice == 1:
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            count = 1
            for product in product_list:
                print(
                    f"{count}. Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Số lượng: {product['quantity']}"
                )
                count += 1

    elif choice == 2:
        product_id = input("Nhập mã sản phẩm: ").strip().upper()
        for product in product_list:
            if product["product_id"] == product_id:
                print("Mã sản phẩm bị trùng")
                break

        else:
            product_name = input("Nhập tên sản phẩm: ")
            price = input("Nhập giá sản phẩm: ")
            quantity = input("Nhập số lượng sản phẩm: ")

            if not price.isdigit() or int(price) <= 0:
                print("Giá/Số lượng không hợp lệ")

            elif not quantity.isdigit() or int(quantity) <= 0:
                print("Giá/Số lượng không hợp lệ")

            else:
                product_list.append({"product_id": product_id,"product_name": product_name,"price": int(price),"quantity": int(quantity)})
                print("Thêm sản phẩm thành công")

    elif choice == 3:
        update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

        for product in product_list:
            if product["product_id"] == update_id:
                new_name = input("Nhập tên sản phẩm mới: ")
                new_price = input("Nhập giá mới: ")
                new_quantity = input("Nhập số lượng mới: ")

                if not new_price.isdigit() or int(new_price) <= 0:
                    print("Giá/Số lượng không hợp lệ")
                    break

                if not new_quantity.isdigit() or int(new_quantity) <= 0:
                    print("Giá/Số lượng không hợp lệ")
                    break

                product["product_name"] = new_name
                product["price"] = int(new_price)
                product["quantity"] = int(new_quantity)
                print("Cập nhật sản phẩm thành công")
                break
        else:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")

    elif choice == 4:
        delete_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip().upper()

        for product in product_list:
            if product["product_id"] == delete_id:
                product_list.remove(product)
                print("Xóa sản phẩm thành công")
                break
        else:
            print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == 5:
        print("Thoát chương trình")
        break