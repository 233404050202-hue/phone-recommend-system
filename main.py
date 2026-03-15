import main1
import main2

print("Chọn mô hình gợi ý:")
print("1 - Content-Based")
print("2 - Collaborative Filtering")

choice = input("Nhập lựa chọn (1 hoặc 2): ")

if choice == "1":
    main1.main()

elif choice == "2":
    main2.main()

else:
    print("Lựa chọn không hợp lệ.")