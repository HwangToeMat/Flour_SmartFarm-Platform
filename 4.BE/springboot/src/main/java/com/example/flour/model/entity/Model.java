package com.example.flour.model.entity;

import lombok.*;
import lombok.experimental.Accessors;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@NoArgsConstructor
@AllArgsConstructor
@Data
@Entity
@ToString(exclude = {"engineer", "modelDetailList"})
@Builder
@Accessors(chain = true)
public class Model {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String version;

    private String content;

    private Integer price;

    private LocalDateTime registeredAt;

    private LocalDateTime unregisteredAt;

    private LocalDateTime updatedAt;

    private String updatedBy;

    @ManyToOne
    private Engineer engineer;

    @OneToMany(fetch = FetchType.LAZY, mappedBy = "model")
    private List<ModelDetail> modelDetailList;

}
