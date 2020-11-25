package com.example.flour.model.network;


import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Header<T> {

    private String transactionTime;

    private String resultCode;

    private String description;

    private T data;
}
