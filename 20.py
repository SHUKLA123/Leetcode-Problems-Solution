  def isValid(self, s: str) -> bool:
      def is_valid(e):
        st = []
        for i in e:
          if i in "({[":
            st.append(i)
          elif i in "})]":
            if st == []:
              return False
            else:
              ch = st.pop()
              if not check(ch,i):
                return False      
        if st == []:
          return True
        else: 
          return False
      def check(ch,i):
        if ch == "(" and i == ")":
          return True
        if ch == "[" and i == "]":
          return True        
        if ch == "{" and i == "}":
          return True
        return False

      return is_valid(s)