要求三:
1.insert into member(name,username,password,follower_count) values('小美','test','test',5);
insert into member(name,username,password,follower_count) values('小林','test2','12524',10);
insert into member(name,username,password,follower_count) values('小蔡','test3','252383',2);
insert into member(name,username,password,follower_count) values('小王','test4','14282',70);
insert into member(name,username,password,follower_count) values('小山','test5','2873272',100);
![1](https://user-images.githubusercontent.com/106290448/197399620-33e3fd2e-1b8a-410c-a3e0-c4186a2598d6.png)

2.select*from member;
![2](https://user-images.githubusercontent.com/106290448/197399641-54f75ae2-9a8e-482b-a1b1-50c429a57bf8.png)

3.select*from member order by time desc;
![3](https://user-images.githubusercontent.com/106290448/197399691-5fdb6fe3-d3af-4f4a-804b-4d8715b2a462.png)

4.select*from member order by time desc limit 1,3;
![4](https://user-images.githubusercontent.com/106290448/197399697-ba157949-0821-4e0b-9f13-03a9a135e758.png)

5.select*from member where username="test";
![5](https://user-images.githubusercontent.com/106290448/197399705-300840f2-c73f-4ace-8f16-292756615058.png)

6.select*from member where username="test" and password="test";
![6](https://user-images.githubusercontent.com/106290448/197399716-cf7667e8-daca-42cf-9de1-aaaf8fb66816.png)

7.set SQL_SAFE_UPDATES=0;
update member set name='test2' where username='test';
![7](https://user-images.githubusercontent.com/106290448/197399729-f6c9700f-de7f-4e00-9655-e43c29306dbb.png)

要求四:
1.select count( * ) as "總共有幾筆資料(幾位會員)" from member;
![8](https://user-images.githubusercontent.com/106290448/197399738-1b501a7d-9cef-493f-abf1-dbe13ca29da5.png)

2.select sum(follower_count) as "所有會員 follower_count 欄位的總和" from member;
![9](https://user-images.githubusercontent.com/106290448/197399742-ce705e83-d71b-4a02-9305-28141dd7ca87.png)

3.select avg(follower_count) as "所有會員 follower_count 欄位的平均數" from member;
![10](https://user-images.githubusercontent.com/106290448/197399747-2c2c025f-5ef3-42fa-82ad-3b1137b69e04.png)
