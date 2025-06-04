<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.1.5</version> <!-- You can adjust this version to your project -->
    <relativePath/>
</parent>

<groupId>com.pawsos</groupId>
<artifactId>pawsos-backend</artifactId>
<version>0.0.1-SNAPSHOT</version>
<name>pawsos</name>
<description>Emergency pet care platform</description>

    <properties>
    <java.version>17</java.version>
    <maven.compiler.source>${java.version}</maven.compiler.source>
    <maven.compiler.target>${java.version}</maven.compiler.target>

    <!-- SonarQube Configuration -->
    <sonar.projectKey>pawsos-group21-pawsos-backend</sonar.projectKey>
    <sonar.projectName>pawsos-backend</sonar.projectName>

    <sonar.coverage.exclusions>
        src/main/java/com/pawsos/pawsosbackend/entity/**,
        src/main/java/com/pawsos/pawsosbackend/dto/**,
        src/main/java/com/pawsos/pawsosbackend/utility/**,
        src/main/java/com/pawsos/pawsosbackend/PawsosApplication*,
        src/main/java/com/pawsos/pawsosbackend/repository/**,
        src/main/java/com/pawsos/pawsosbackend/controller/**,
        src/main/java/com/pawsos/pawsosbackend/config/**
    </sonar.coverage.exclusions>

    <!-- The below lines ensure the build fails if quality gate fails -->
    <sonar.qualitygate.wait>true</sonar.qualitygate.wait>
    <sonar.qualitygate.failOnSonarQubeExitCode>true</sonar.qualitygate.failOnSonarQubeExitCode>

    <sonar.sources>${project.basedir}/src/main/java</sonar.sources>
    <sonar.tests>${project.basedir}/src/test/java</sonar.tests>
    <sonar.java.binaries>${project.basedir}/target/classes</sonar.java.binaries>
    <sonar.junit.reportsPath>${project.basedir}/target/surefire-reports</sonar.junit.reportsPath>
    <sonar.java.coveragePlugin>jacoco</sonar.java.coveragePlugin>
    <sonar.coverage.jacoco.xmlReportPaths>${project.basedir}/target/jacoco-ut/jacoco.xml</sonar.coverage.jacoco.xmlReportPaths>
</properties>

<dependencies>
    <!-- Spring Boot Core -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- Spring Boot JPA -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>

    <!-- Spring Boot Security -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security</artifactId>
    </dependency>

    <!-- Validation -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-validation</artifactId>
    </dependency>

    <!-- MySQL -->
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <scope>runtime</scope>
    </dependency>

    <!-- Lombok -->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>

    <!-- Devtools (Optional for Live Reload) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
        <scope>runtime</scope>
        <optional>true</optional>
    </dependency>

    <!-- JUnit for Testing -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

    <!-- Spring Security Test -->
    <dependency>
        <groupId>org.springframework.security</groupId>
        <artifactId>spring-security-test</artifactId>  
        <scope>test</scope>
    </dependency>

    <!-- Mockito -->
    <dependency>
        <groupId>org.mockito</groupId>
        <artifactId>mockito-core</artifactId>
        <scope>test</scope>
    </dependency>

    <dependency>
        <groupId>org.mockito</groupId>
        <artifactId>mockito-junit-jupiter</artifactId>
        <scope>test</scope>
    </dependency>

</dependencies>

<build>
 <finalName>pawsos-backend</finalName>
    <plugins>
        <!-- Compiler Plugin -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <configuration>
                <source>${java.version}</source>
                <target>${java.version}</target>
                <annotationProcessorPaths>
                    <path>
                        <groupId>org.projectlombok</groupId>
                        <artifactId>lombok</artifactId>
                        <version>1.18.30</version>
                    </path>
                </annotationProcessorPaths>
            </configuration>
        </plugin>
		            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <configuration>
                    <failIfNoTests>false</failIfNoTests>
                    <testFailureIgnore>false</testFailureIgnore>
                </configuration>
            </plugin>

            <!-- PMD plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-pmd-plugin</artifactId>
                <version>3.22.0</version>
                <configuration>
                    <excludes></excludes>
                    <rulesets>
                        <ruleset>${project.basedir}/RuleSet.xml</ruleset>
                    </rulesets>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>

            <!-- Code Coverage Plugin -->
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <version>0.8.11</version>
                <configuration>
                    <excludes>
                        <exclude>com/pawsos/pawsosbackend/controller/**</exclude>
                        <exclude>com/pawsos/pawsosbackend/utility/**</exclude>
                        <exclude>com/pawsos/pawsosbackend/dto/**</exclude>
                        <exclude>com/pawsos/pawsosbackend/entity/**</exclude>
                        <exclude>com/pawsos/pawsosbackend/security/**</exclude>
                        <exclude>com/pawsos/pawsosbackend/repository/**</exclude>
                        <exclude>com/pawsos/pawsosbackend/pawsos*</exclude>
                    </excludes>
                </configuration>
                <executions>
                    <execution>
                        <id>report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report</goal>
                        </goals>
                    </execution>
                    <execution>
                        <id>report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report</goal>
                        </goals>
                    </execution>
                    <execution>
                        <id>coverage-check</id>
                        <goals>
                            <goal>check</goal>
                        </goals>
                        <configuration>
                            <rules>
                                <rule>
                                    <element>CLASS</element>
                                    <limits>
                                        <limit>
                                            <counter>LINE</counter>
                                            <value>COVEREDRATIO</value>
                                            <minimum>0.0</minimum>
                                        </limit>
                                    </limits>
                                </rule>
                            </rules>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
              <plugin>
                <groupId>org.sonarsource.scanner.maven</groupId>
                <artifactId>sonar-maven-plugin</artifactId>
                <version>3.10.0.2594</version>
            </plugin>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <excludes>
                    <exclude>
                        <groupId>org.projectlombok</groupId>
                        <artifactId>lombok</artifactId>
                    </exclude>
                </excludes>
            </configuration>
        </plugin>
    </plugins>
</build>
</project>
