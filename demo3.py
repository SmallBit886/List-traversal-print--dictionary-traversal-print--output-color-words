'''输出体重指标'''
height=185
weight=72.5
bmi=weight/(height+weight)
print('您的身体指标是：',bmi)
#print('您的身体指标是：'+bmi)#TypeError: can only concatenate str (not "float") to str
print('您的身体指标是：'+str(bmi))#您的身体指标是：0.2815533980582524
print('您的BMI指标是：'+'{:0.2f}'.format(bmi))#您的BMI指标是：0.28