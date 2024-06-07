using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class MoveCharacterController : MonoBehaviour
{
    //private float speed = 0.08f;
    // あらかじめ Animator コンポーネントを持っておくようにする
    private Animator _animator;

    // Start is called before the first frame update
    void Start()
    {
     // オブジェクトに紐付いている Animator を取得する
    _animator = GetComponent<Animator>();

    // 最初のプレイヤーの向き (下) を設定する
    _animator.SetFloat("X", 0);
    _animator.SetFloat("Y", -1);
    }

    // Update is called once per frame
    void Update()
    {
        // キーボードの入力方向を取得
        var move = GetMove();

        if (move != Vector2.zero)
        {
        // 入力されている場合はアニメーターに方向を設定
        _animator.SetFloat("X", move.x);
        _animator.SetFloat("Y", move.y);

        //入力した方向に移動
        transform.Translate(move * Time.deltaTime*4);//0.1f);
        }
        /*
        Vector2 position = transform.position;

        if (Input.GetKey("left"))
        {
            position.x -= speed;
        }
        else if (Input.GetKey("right"))
        {
            position.x += speed;
        }
        else if (Input.GetKey("up"))
        {
            position.y += speed;
        }
        else if (Input.GetKey("down"))
        {
            position.y -= speed;
        }

        transform.position = position;
        }*/
    }

  /// <summary>キーボード入力による移動方向を取得します。</summary>
  /// <returns>キーボード入力による移動方向。</returns>
  private Vector2 GetMove()
  {
    Vector2 move = Vector2.zero;
    if (Keyboard.current.upArrowKey.isPressed)
    {
      move += new Vector2(0, 1);
    }
    if (Keyboard.current.downArrowKey.isPressed)
    {
      move += new Vector2(0, -1);
    }
    if (Keyboard.current.leftArrowKey.isPressed)
    {
      this.GetComponent<SpriteRenderer>().flipX = false;
      move += new Vector2(-1, 0);
    }
    if (Keyboard.current.rightArrowKey.isPressed)
    {
      this.GetComponent<SpriteRenderer>().flipX = true;
      move += new Vector2(1, 0);
    }

    // 入力した値がある場合は正規化して返す
    return move == Vector2.zero ? move : move.normalized;
  }
}
