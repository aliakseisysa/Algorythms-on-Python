#!/usr/bin/env python
# coding: utf-8

# # Задание

# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.

# In[1]:


import hashlib  


# In[77]:


def sub_str(s: str) -> int:
    assert len(s) > 0, 'Zero strings are forbidden'
    
    h_s = hashlib.sha1(s.encode('utf-8')).hexdigest()
    len_subs = range(1,len(s))
    count = 0
    
    for i in range(len(s)):
        for j in len_subs:
            if h_s != hashlib.sha1(s[i:i + j].encode('utf-8')).hexdigest() and hashlib.sha1(s[i:i + j -1].encode('utf-8')).hexdigest() != hashlib.sha1(s[i:i + j].encode('utf-8')).hexdigest():
                #print(s[i:i + j])
                #print(hashlib.sha1(s[i:i + j].encode('utf-8')).hexdigest())
                count += 1
        
    return count


# In[80]:


s_1 = input('Введите строку: ')


# In[81]:


nums = sub_str(s_1)


# In[82]:


print(f'Количество различных подстрок в строке равно {nums}')


# In[ ]:




