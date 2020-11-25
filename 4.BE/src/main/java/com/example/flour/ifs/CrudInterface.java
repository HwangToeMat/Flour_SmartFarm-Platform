package com.example.flour.ifs;

import com.example.flour.model.network.Header;

public interface CrudInterface {

    Header create();

    Header read(Long id);

    Header update();

    Header delete(Long id);
}
