"""3.10.1

Revision ID: 4abeb646159c
Revises: 
Create Date: 2024-08-27 10:41:24.065537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4abeb646159c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vadmin_auth_dept',
    sa.Column('name', sa.String(length=50), nullable=False, comment='部门名称'),
    sa.Column('dept_key', sa.String(length=50), nullable=False, comment='部门标识'),
    sa.Column('disabled', sa.Boolean(), nullable=False, comment='是否禁用'),
    sa.Column('order', sa.Integer(), nullable=True, comment='显示排序'),
    sa.Column('desc', sa.String(length=255), nullable=True, comment='描述'),
    sa.Column('owner', sa.String(length=255), nullable=True, comment='负责人'),
    sa.Column('phone', sa.String(length=255), nullable=True, comment='联系电话'),
    sa.Column('email', sa.String(length=255), nullable=True, comment='邮箱'),
    sa.Column('parent_id', sa.Integer(), nullable=True, comment='上级部门'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.ForeignKeyConstraint(['parent_id'], ['vadmin_auth_dept.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    comment='部门表'
    )
    op.create_index(op.f('ix_vadmin_auth_dept_dept_key'), 'vadmin_auth_dept', ['dept_key'], unique=False)
    op.create_index(op.f('ix_vadmin_auth_dept_name'), 'vadmin_auth_dept', ['name'], unique=False)
    op.create_table('vadmin_auth_menu',
    sa.Column('title', sa.String(length=50), nullable=False, comment='名称'),
    sa.Column('icon', sa.String(length=50), nullable=True, comment='菜单图标'),
    sa.Column('redirect', sa.String(length=100), nullable=True, comment='重定向地址'),
    sa.Column('component', sa.String(length=255), nullable=True, comment='前端组件地址'),
    sa.Column('path', sa.String(length=50), nullable=True, comment='前端路由地址'),
    sa.Column('disabled', sa.Boolean(), nullable=False, comment='是否禁用'),
    sa.Column('hidden', sa.Boolean(), nullable=False, comment='是否隐藏'),
    sa.Column('order', sa.Integer(), nullable=False, comment='排序'),
    sa.Column('menu_type', sa.String(length=8), nullable=False, comment='菜单类型'),
    sa.Column('parent_id', sa.Integer(), nullable=True, comment='父菜单'),
    sa.Column('perms', sa.String(length=50), nullable=True, comment='权限标识'),
    sa.Column('noCache', sa.Boolean(), nullable=False, comment='如果设置为true，则不会被 <keep-alive> 缓存(默认 false)'),
    sa.Column('breadcrumb', sa.Boolean(), nullable=False, comment='如果设置为false，则不会在breadcrumb面包屑中显示(默认 true)'),
    sa.Column('affix', sa.Boolean(), nullable=False, comment='如果设置为true，则会一直固定在tag项中(默认 false)'),
    sa.Column('noTagsView', sa.Boolean(), nullable=False, comment='如果设置为true，则不会出现在tag中(默认 false)'),
    sa.Column('canTo', sa.Boolean(), nullable=False, comment='设置为true即使hidden为true，也依然可以进行路由跳转(默认 false)'),
    sa.Column('alwaysShow', sa.Boolean(), nullable=False, comment='当你一个路由下面的 children 声明的路由大于1个时，自动会变成嵌套的模式，\n    只有一个时，会将那个子路由当做根路由显示在侧边栏，若你想不管路由下面的 children 声明的个数都显示你的根路由，\n    你可以设置 alwaysShow: true，这样它就会忽略之前定义的规则，一直显示根路由(默认 true)'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.ForeignKeyConstraint(['parent_id'], ['vadmin_auth_menu.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    comment='菜单表'
    )
    op.create_index(op.f('ix_vadmin_auth_menu_perms'), 'vadmin_auth_menu', ['perms'], unique=False)
    op.create_table('vadmin_auth_role',
    sa.Column('name', sa.String(length=50), nullable=False, comment='名称'),
    sa.Column('role_key', sa.String(length=50), nullable=False, comment='权限字符'),
    sa.Column('data_range', sa.Integer(), nullable=False, comment='数据权限范围'),
    sa.Column('disabled', sa.Boolean(), nullable=False, comment='是否禁用'),
    sa.Column('order', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('desc', sa.String(length=255), nullable=True, comment='描述'),
    sa.Column('is_admin', sa.Boolean(), nullable=False, comment='是否为超级角色'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.PrimaryKeyConstraint('id'),
    comment='角色表'
    )
    op.create_index(op.f('ix_vadmin_auth_role_name'), 'vadmin_auth_role', ['name'], unique=False)
    op.create_index(op.f('ix_vadmin_auth_role_role_key'), 'vadmin_auth_role', ['role_key'], unique=False)
    op.create_table('vadmin_auth_user',
    sa.Column('avatar', sa.String(length=500), nullable=True, comment='头像'),
    sa.Column('telephone', sa.String(length=11), nullable=False, comment='手机号'),
    sa.Column('email', sa.String(length=50), nullable=True, comment='邮箱地址'),
    sa.Column('name', sa.String(length=50), nullable=False, comment='姓名'),
    sa.Column('nickname', sa.String(length=50), nullable=True, comment='昵称'),
    sa.Column('password', sa.String(length=255), nullable=True, comment='密码'),
    sa.Column('gender', sa.String(length=8), nullable=True, comment='性别'),
    sa.Column('is_active', sa.Boolean(), nullable=False, comment='是否可用'),
    sa.Column('is_reset_password', sa.Boolean(), nullable=False, comment='是否已经重置密码，没有重置的，登陆系统后必须重置密码'),
    sa.Column('last_ip', sa.String(length=50), nullable=True, comment='最后一次登录IP'),
    sa.Column('last_login', sa.DateTime(), nullable=True, comment='最近一次登录时间'),
    sa.Column('is_staff', sa.Boolean(), nullable=False, comment='是否为工作人员'),
    sa.Column('wx_server_openid', sa.String(length=255), nullable=True, comment='服务端微信平台openid'),
    sa.Column('is_wx_server_openid', sa.Boolean(), nullable=False, comment='是否已有服务端微信平台openid'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.PrimaryKeyConstraint('id'),
    comment='用户表'
    )
    op.create_index(op.f('ix_vadmin_auth_user_name'), 'vadmin_auth_user', ['name'], unique=False)
    op.create_index(op.f('ix_vadmin_auth_user_telephone'), 'vadmin_auth_user', ['telephone'], unique=False)
    op.create_table('vadmin_record_login',
    sa.Column('telephone', sa.String(length=255), nullable=False, comment='手机号'),
    sa.Column('status', sa.Boolean(), nullable=False, comment='是否登录成功'),
    sa.Column('platform', sa.String(length=8), nullable=False, comment='登陆平台'),
    sa.Column('login_method', sa.String(length=8), nullable=False, comment='认证方式'),
    sa.Column('ip', sa.String(length=50), nullable=True, comment='登陆地址'),
    sa.Column('address', sa.String(length=255), nullable=True, comment='登陆地点'),
    sa.Column('country', sa.String(length=255), nullable=True, comment='国家'),
    sa.Column('province', sa.String(length=255), nullable=True, comment='县'),
    sa.Column('city', sa.String(length=255), nullable=True, comment='城市'),
    sa.Column('county', sa.String(length=255), nullable=True, comment='区/县'),
    sa.Column('operator', sa.String(length=255), nullable=True, comment='运营商'),
    sa.Column('postal_code', sa.String(length=255), nullable=True, comment='邮政编码'),
    sa.Column('area_code', sa.String(length=255), nullable=True, comment='地区区号'),
    sa.Column('browser', sa.String(length=50), nullable=True, comment='浏览器'),
    sa.Column('system', sa.String(length=50), nullable=True, comment='操作系统'),
    sa.Column('response', sa.Text(), nullable=True, comment='响应信息'),
    sa.Column('request', sa.Text(), nullable=True, comment='请求信息'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.PrimaryKeyConstraint('id'),
    comment='登录记录表'
    )
    op.create_index(op.f('ix_vadmin_record_login_telephone'), 'vadmin_record_login', ['telephone'], unique=False)
    op.create_table('vadmin_system_dict_type',
    sa.Column('dict_name', sa.String(length=50), nullable=False, comment='字典名称'),
    sa.Column('dict_type', sa.String(length=50), nullable=False, comment='字典类型'),
    sa.Column('disabled', sa.Boolean(), nullable=False, comment='字典状态，是否禁用'),
    sa.Column('remark', sa.String(length=255), nullable=True, comment='备注'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.PrimaryKeyConstraint('id'),
    comment='字典类型表'
    )
    op.create_index(op.f('ix_vadmin_system_dict_type_dict_name'), 'vadmin_system_dict_type', ['dict_name'], unique=False)
    op.create_index(op.f('ix_vadmin_system_dict_type_dict_type'), 'vadmin_system_dict_type', ['dict_type'], unique=False)
    op.create_table('vadmin_system_settings_tab',
    sa.Column('title', sa.String(length=255), nullable=False, comment='标题'),
    sa.Column('classify', sa.String(length=255), nullable=False, comment='分类键'),
    sa.Column('tab_label', sa.String(length=255), nullable=False, comment='tab标题'),
    sa.Column('tab_name', sa.String(length=255), nullable=False, comment='tab标识符'),
    sa.Column('hidden', sa.Boolean(), nullable=False, comment='是否隐藏'),
    sa.Column('disabled', sa.Boolean(), nullable=False, comment='是否禁用'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.PrimaryKeyConstraint('id'),
    comment='系统配置分类表'
    )
    op.create_index(op.f('ix_vadmin_system_settings_tab_classify'), 'vadmin_system_settings_tab', ['classify'], unique=False)
    op.create_index(op.f('ix_vadmin_system_settings_tab_tab_name'), 'vadmin_system_settings_tab', ['tab_name'], unique=True)
    op.create_table('vadmin_auth_role_depts',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('dept_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dept_id'], ['vadmin_auth_dept.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['vadmin_auth_role.id'], ondelete='CASCADE')
    )
    op.create_table('vadmin_auth_role_menus',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('menu_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['vadmin_auth_menu.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['vadmin_auth_role.id'], ondelete='CASCADE')
    )
    op.create_table('vadmin_auth_user_depts',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('dept_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dept_id'], ['vadmin_auth_dept.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['vadmin_auth_user.id'], ondelete='CASCADE')
    )
    op.create_table('vadmin_auth_user_roles',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['vadmin_auth_role.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['vadmin_auth_user.id'], ondelete='CASCADE')
    )
    op.create_table('vadmin_help_issue_category',
    sa.Column('name', sa.String(length=50), nullable=False, comment='类别名称'),
    sa.Column('platform', sa.String(length=8), nullable=False, comment='展示平台'),
    sa.Column('is_active', sa.Boolean(), nullable=False, comment='是否可见'),
    sa.Column('create_user_id', sa.Integer(), nullable=False, comment='创建人'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.ForeignKeyConstraint(['create_user_id'], ['vadmin_auth_user.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    comment='常见问题类别表'
    )
    op.create_index(op.f('ix_vadmin_help_issue_category_name'), 'vadmin_help_issue_category', ['name'], unique=False)
    op.create_index(op.f('ix_vadmin_help_issue_category_platform'), 'vadmin_help_issue_category', ['platform'], unique=False)
    op.create_table('vadmin_record_sms_send',
    sa.Column('user_id', sa.Integer(), nullable=False, comment='操作人'),
    sa.Column('status', sa.Boolean(), nullable=False, comment='发送状态'),
    sa.Column('content', sa.String(length=255), nullable=False, comment='发送内容'),
    sa.Column('telephone', sa.String(length=11), nullable=False, comment='目标手机号'),
    sa.Column('desc', sa.String(length=255), nullable=True, comment='失败描述'),
    sa.Column('scene', sa.String(length=50), nullable=True, comment='发送场景'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.ForeignKeyConstraint(['user_id'], ['vadmin_auth_user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    comment='短信发送记录表'
    )
    op.create_table('vadmin_resource_images',
    sa.Column('filename', sa.String(length=255), nullable=False, comment='原图片名称'),
    sa.Column('image_url', sa.String(length=500), nullable=False, comment='图片链接'),
    sa.Column('create_user_id', sa.Integer(), nullable=False, comment='创建人'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.ForeignKeyConstraint(['create_user_id'], ['vadmin_auth_user.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    comment='图片素材表'
    )
    op.create_table('vadmin_system_dict_details',
    sa.Column('label', sa.String(length=50), nullable=False, comment='字典标签'),
    sa.Column('value', sa.String(length=50), nullable=False, comment='字典键值'),
    sa.Column('disabled', sa.Boolean(), nullable=False, comment='字典状态，是否禁用'),
    sa.Column('is_default', sa.Boolean(), nullable=False, comment='是否默认'),
    sa.Column('order', sa.Integer(), nullable=False, comment='字典排序'),
    sa.Column('dict_type_id', sa.Integer(), nullable=False, comment='关联字典类型'),
    sa.Column('remark', sa.String(length=255), nullable=True, comment='备注'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.ForeignKeyConstraint(['dict_type_id'], ['vadmin_system_dict_type.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    comment='字典详情表'
    )
    op.create_index(op.f('ix_vadmin_system_dict_details_label'), 'vadmin_system_dict_details', ['label'], unique=False)
    op.create_index(op.f('ix_vadmin_system_dict_details_value'), 'vadmin_system_dict_details', ['value'], unique=False)
    op.create_table('vadmin_system_settings',
    sa.Column('config_label', sa.String(length=255), nullable=False, comment='配置表标签'),
    sa.Column('config_key', sa.String(length=255), nullable=False, comment='配置表键'),
    sa.Column('config_value', sa.Text(), nullable=True, comment='配置表内容'),
    sa.Column('remark', sa.String(length=255), nullable=True, comment='备注信息'),
    sa.Column('disabled', sa.Boolean(), nullable=False, comment='是否禁用'),
    sa.Column('tab_id', sa.Integer(), nullable=False, comment='关联tab标签'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.ForeignKeyConstraint(['tab_id'], ['vadmin_system_settings_tab.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    comment='系统配置表'
    )
    op.create_index(op.f('ix_vadmin_system_settings_config_key'), 'vadmin_system_settings', ['config_key'], unique=True)
    op.create_table('vadmin_help_issue',
    sa.Column('category_id', sa.Integer(), nullable=False, comment='类别'),
    sa.Column('title', sa.String(length=255), nullable=False, comment='标题'),
    sa.Column('content', sa.Text(), nullable=False, comment='内容'),
    sa.Column('view_number', sa.Integer(), nullable=False, comment='查看次数'),
    sa.Column('is_active', sa.Boolean(), nullable=False, comment='是否可见'),
    sa.Column('create_user_id', sa.Integer(), nullable=False, comment='创建人'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.ForeignKeyConstraint(['category_id'], ['vadmin_help_issue_category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['create_user_id'], ['vadmin_auth_user.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    comment='常见问题记录表'
    )
    op.create_index(op.f('ix_vadmin_help_issue_title'), 'vadmin_help_issue', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vadmin_help_issue_title'), table_name='vadmin_help_issue')
    op.drop_table('vadmin_help_issue')
    op.drop_index(op.f('ix_vadmin_system_settings_config_key'), table_name='vadmin_system_settings')
    op.drop_table('vadmin_system_settings')
    op.drop_index(op.f('ix_vadmin_system_dict_details_value'), table_name='vadmin_system_dict_details')
    op.drop_index(op.f('ix_vadmin_system_dict_details_label'), table_name='vadmin_system_dict_details')
    op.drop_table('vadmin_system_dict_details')
    op.drop_table('vadmin_resource_images')
    op.drop_table('vadmin_record_sms_send')
    op.drop_index(op.f('ix_vadmin_help_issue_category_platform'), table_name='vadmin_help_issue_category')
    op.drop_index(op.f('ix_vadmin_help_issue_category_name'), table_name='vadmin_help_issue_category')
    op.drop_table('vadmin_help_issue_category')
    op.drop_table('vadmin_auth_user_roles')
    op.drop_table('vadmin_auth_user_depts')
    op.drop_table('vadmin_auth_role_menus')
    op.drop_table('vadmin_auth_role_depts')
    op.drop_index(op.f('ix_vadmin_system_settings_tab_tab_name'), table_name='vadmin_system_settings_tab')
    op.drop_index(op.f('ix_vadmin_system_settings_tab_classify'), table_name='vadmin_system_settings_tab')
    op.drop_table('vadmin_system_settings_tab')
    op.drop_index(op.f('ix_vadmin_system_dict_type_dict_type'), table_name='vadmin_system_dict_type')
    op.drop_index(op.f('ix_vadmin_system_dict_type_dict_name'), table_name='vadmin_system_dict_type')
    op.drop_table('vadmin_system_dict_type')
    op.drop_index(op.f('ix_vadmin_record_login_telephone'), table_name='vadmin_record_login')
    op.drop_table('vadmin_record_login')
    op.drop_index(op.f('ix_vadmin_auth_user_telephone'), table_name='vadmin_auth_user')
    op.drop_index(op.f('ix_vadmin_auth_user_name'), table_name='vadmin_auth_user')
    op.drop_table('vadmin_auth_user')
    op.drop_index(op.f('ix_vadmin_auth_role_role_key'), table_name='vadmin_auth_role')
    op.drop_index(op.f('ix_vadmin_auth_role_name'), table_name='vadmin_auth_role')
    op.drop_table('vadmin_auth_role')
    op.drop_index(op.f('ix_vadmin_auth_menu_perms'), table_name='vadmin_auth_menu')
    op.drop_table('vadmin_auth_menu')
    op.drop_index(op.f('ix_vadmin_auth_dept_name'), table_name='vadmin_auth_dept')
    op.drop_index(op.f('ix_vadmin_auth_dept_dept_key'), table_name='vadmin_auth_dept')
    op.drop_table('vadmin_auth_dept')
    # ### end Alembic commands ###
