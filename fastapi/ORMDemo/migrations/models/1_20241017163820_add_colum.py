from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `addr` VARCHAR(100) NOT NULL  COMMENT '教室';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP COLUMN `addr`;"""
