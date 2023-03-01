<?php 

namespace web\models;

/**
 * 违直播关联表
 * Class RoomRecordLk
 *
 * @property $id * @property $il_id * @property $vod_id * @property $status * @property $created_at * @property $updated_at * @property $deleted_at
 *
 * @package Core\Models
 */

class RoomRecordLk extends \vhallComponent\access\models\AccessModel
{
    protected $table = "room_record_lk";

    // 推流状态 未推流    // （默认）    const STATUS_1 = 1;    // 推流成功    const STATUS_2 = 2;    // 推流失败    const STATUS_3 = 3;

}

