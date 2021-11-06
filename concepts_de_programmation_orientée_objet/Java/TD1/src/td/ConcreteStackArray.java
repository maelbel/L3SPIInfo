package td;

import java.util.ArrayList;

public class ConcreteStackArray implements AStack{
    private ArrayList<Object> ListO ;


    public ConcreteStackArray() {
        ListO = new ArrayList<Object>();
    }
    @Override
    public boolean isEmpty() {
        return ListO.isEmpty();
    }

    @Override
    public void push(Object obj) {
        ListO.add(obj);
    }

    @Override
    public Object peek() {
        Object res = null;
        if (!this.isEmpty()){
            res = ListO.get(ListO.size()-1);
        }return res;
    }

    @Override
    public Object pop() {
        Object res = null;
        if (!this.isEmpty()){
            res = ListO.remove(ListO.size()-1);
        }return res;
    }
}