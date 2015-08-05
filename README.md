# MyEnrich
Record what I do everyday to enrich my life.

## 功能
- 记录当日里程碑
- 查看往日里程碑
- 修改往日里程碑
- 删除往日里程碑

## 包依赖
* python == 2.7.9
* Django == 1.6.5
* bootstrap == 3.0.0
* jquery == 1.10.2
* flat-ui == unknown
* jquery.timelinr == 0.9.53
* jquery.wookmark == unknown

## 效果展示
- 记录今日里程碑
<img src='/pic/milestone.jpg' width=750 />

- 往日里程碑展示
<img src='/pic/history.jpg' width=750 />

- 空里程碑展示
<img src='/pic/no-history.jpg' width=750 />

## 注
- [Django静态文件配置](http://blog.csdn.net/hireboy/article/details/8806098)
- 部署SAE步骤
  1. 更新SAE生成的index.wsgi
  2. 更新SAE生成的config.yaml（如果没有用SAE带的python库，这块不更新）
  3. 更新settings.py （包括SAE头文件，变量定义，数据库）
  4. 自建site-packages包
- 数据库及superuser 用户名[admin] 密码[admin]
