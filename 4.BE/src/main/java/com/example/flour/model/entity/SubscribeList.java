package com.example.flour.model.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import javax.persistence.*;
import java.math.BigDecimal;
import java.util.List;

@NoArgsConstructor
@AllArgsConstructor
@Data
@Entity
@ToString(exclude = {"modelDetailList", "user"})
public class SubscribeList {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String status;

    private String subscribeType;

    private String paymentType; // 카드 / 현금

    private BigDecimal totalPrice;

    private Integer totalQuantity;

    @OneToOne(fetch = FetchType.LAZY, mappedBy = "subscribeList")
    private User user;

    @OneToMany(fetch = FetchType.LAZY, mappedBy = "subscribeList")
    private List<ModelDetail> modelDetailList;
}
