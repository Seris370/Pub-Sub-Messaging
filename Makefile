setup:
	python3 setup.py

pub1:
	docker run --interactive --network pubsub-messaging_default confluentinc/cp-kafkacat kafkacat -b kafka1:9092 -t new_topic -P

pub2:
	docker run --interactive --network pubsub-messaging_default confluentinc/cp-kafkacat kafkacat -b kafka2:9092 -t new_topic -P

pub3:
	docker run --interactive --network pubsub-messaging_default confluentinc/cp-kafkacat kafkacat -b kafka3:9092 -t new_topic -P

sub1:
	docker run --tty --network pubsub-messaging_default confluentinc/cp-kafkacat kafkacat -b kafka1:9092 -t new_topic -C

sub2:
	docker run --tty --network pubsub-messaging_default confluentinc/cp-kafkacat kafkacat -b kafka2:9092 -t new_topic -C

sub3:
	docker run --tty --network pubsub-messaging_default confluentinc/cp-kafkacat kafkacat -b kafka3:9092 -t new_topic -C

list:
	docker run --tty --network pubsub-messaging_default confluentinc/cp-kafkacat kafkacat -b kafka1:9092 -t new_topic -L
