package com.example.flour.model.entity;

import lombok.*;
import lombok.experimental.Accessors;

import javax.persistence.*;
import java.math.BigDecimal;
import java.util.List;

@NoArgsConstructor
@AllArgsConstructor
@Data
@Entity
@ToString(exclude = {"modelDetailList", "user"})
@Builder
@Accessors(chain = true)
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
