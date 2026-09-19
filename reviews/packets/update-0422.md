<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0422.txt",
      "sha256": "9ae7d86d0ecccc897dc5d06824b2e3e909e8a300479ea36200def6c266a68e00",
      "bytes": 12650
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8950444aff41cccd8f4b45b486101f1b825d29ac24147aec86b9efecf596e5c3",
      "bytes": 2174
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b86886be1e7715485612ee8679a0961b6d7917b8691159c8cdd0f00d4fb20687",
      "bytes": 139155
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cf146011b520276f551860d375af472af9799a84c597ae7e68faf44199db66a1",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2b4ea10f6d05d6cc633cab80a2057f7d318a66502b9003b69642c69c8b20dd2a",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "370b0a5f50119c5a5bdef457d93acfc66121372ea5c165bb062578a4fe606be3",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ecd433f971b2317219d4438c1b6db45f30e05d3ce0788d56c570358596941f56",
      "bytes": 128783
    }
  ],
  "estimated_tokens": 9056
}
-->

# Durable State Update — Chapter 422

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 422. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 422. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 422,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 422,
    "continuity_sources": [422],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Arch Lich has appeared before Jin and claims authority over all undead monsters.",
    "The Arch Lich can observe Jin through Familiars and protect itself from Qi Sense with an unidentified powerful force.",
    "The Arch Lich seeks to corrupt Jin, whose soul and death energy it considers unusually powerful.",
    "The Arch Lich repelled Jin's White Flame attack with Gravity before the spear could reach it.",
    "The Arch Lich claims to serve the great king Asmodeus, whose current status and location remain unknown.",
    "Jin experienced a sixth-sense insight that let him distinguish magical illusions from their underlying essence and destroy the true Bone Spears with Heavenly Strike.",
    "Jin is temporarily afflicted by Curse, which reduced Strength and Stamina by 20 and whose duration is unresolved.",
    "The Arch Lich corrupted Lei Fei into the Death Knight Lord after Lei Fei's death.",
    "Choi Minwoo trusts Jin deeply and leads the allied fighters against the monsters.",
    "The city's transformation into one enormous Gate remains an active threat.",
    "The Skeleton Warlord remains intensely frightened by the Arch Lich, with the cause still unexplained.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    421
  ],
  "open_questions": [
    "Can Jin and the allied Hunters stop the city's transformation into a Gate?",
    "What is the full extent of the Arch Lich's power and ability to observe or identify Jin?",
    "What is Asmodeus's current status and location?",
    "Why does the Skeleton Warlord react to the Arch Lich with such extreme fear?"
  ],
  "safe_through": 421,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 마계 as Demon Realm.",
    "Render 데스나이트 로드 as Death Knight Lord.",
    "Render 마왕 아스모데우스 as Demon King Asmodeus and 전하 as His Highness.",
    "Preserve Jin's profanity and the Arch Lich's archaic, taunting register; render its spells as Gravity, Dark Hand, Curse, Dark Vine, and Bone Spear."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 대적자 | **the Adversary** | Ancient human enemy remembered by the Arch Lich. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 420
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 421
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 421
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃422화



띠링. 띠링. 띠링.



- 위기 속에 기회가 있는 법. 당신은 생사가 오가는 전투 속에서 새로운 깨달음을 얻었습니다!

- [중단전(中丹田)]이 개방되었습니다!

- [중단전]의 개방으로 모든 능력치가 20씩 상승합니다!

- [운기조식]의 효과가 대폭 향상되었습니다!

- 기의 흐름을 파악하고 운용하는 능력이 대폭 향상되었습니다!

- 근골과 근맥이 상승했습니다!

.

.

.



쉼 없이 귓가를 파고드는 시스템 알림.

한 줄기 바람이 땀에 젖은 머리칼을 흔들었고, 나는 전신에 스며드는 새로운 힘과 변화를 느꼈다.

마지막에 울려 퍼진 맑은 종소리까지도.

띠링.



- 깨달음에 대한 보상으로 대량의 경험치를 획득했습니다!

- 깨달음에 대한 보상으로 50포인트를 획득했습니다!

- 레벨 업!

- 레벨 업의 효과로 모든 상태 이상과 피로, 일부 부상이 회복됩니다!

- 상태 이상, [저주]가 해제되었습니다!

- 일시적으로 하락했던 능력치가 원상복구 되었습니다!



그리고 이와 같은 변화를 느낀 것은 나뿐만이 아니었다.

손이 하는 일을 주인이 모를 수는 없는 법. 자신의 저주 마법이 풀린 것을 깨달은 아크 리치가 불신 어린 음성으로 물었다.

- 도대체 어떻게?

놈이 현재 느끼는 모든 의문이 함축된 한마디에, 나는 어깨를 으쓱해 보였다.

“잘.”

- 잘?

“그래, 잘.”

- 그것으로 설명이 된다고 생각하나?

“당연히 아니지. 그런데 내가 그것까지 설명해 줘야 하나?”

잘게 흔들리는 안광으로부터 어처구니없어하는 감정이 고스란히 전해졌다.

- 분명 넌 마법사가 아닐 텐데?

“마법사가 되고 싶긴 했지. 걔들 수당이 더 높거든. 그런데 재능이 없더라고. 머리도 안 좋고.”

- 너희가 대마도사라 부르는 그 인간들조차 내 마법을 이리 쉽게 파훼할 수는 없다.

“없는데요, 됐습니다.”

- 이 무슨 말도 안 되는!

인정한다.

아크 리치의 마법은, 아니 실력은 나보다 확실히 우위에 있었다.

이미 일반적인 헌터의 한계를 아득하게 뛰어넘은 나조차 놈의 저주 마법을 피할 수 없었고, 본 스피어를 이용한 대규모 환영 마법은 정말이지 위험했다.

깨달음을 얻지 못했다면, 어쩌면 지금 이 자리에 서 있지도 못할 것이다.

하지만…….

“그래서 니가 어쩔 건데.”

- ……!

내게는 시스템이 있고, 나는 내게 주어진 힘과 노력으로 최선을 다하여 위기를 타파했을 뿐이다.

억울하면 자기도 시스템 쓰든가.

“세상일이 원래 다 이런 거야. 기분 더럽고 짜증 나도 적당히 참고 넘어가야지 어쩌겠어. 이미 벌어진 일인데. 안 그래?”

조금 전까지만 해도 비명을 지르고 있던 스켈레톤 워로드가 중얼거렸다.

- 와, 말 진짜 예쁘게 한다.

내가 좀 그런 편이지.

- 그런데 간악한 인간이여. 저놈은 적당히 참고 넘어갈 생각이 없어 보이는데.

스켈레톤 워로드의 말이 맞았다.

다음 순간, 엄청난 마력의 회오리와 함께 스산한 음성이 울려 퍼졌으니까.

- 터트려라. 소닉 바스터(Sonic Buster).

그리고 동시에.

쏴아아악, 퍼엉!

고도로 응축된 바람이 일시에 터져 나갔다.

음속의 속도로 쏘아진 바람의 구(球)에 스치는 것만으로 콘크리트가 가루가 되고 철근이 끊어졌다.

여파를 이기지 못한 고층 빌딩의 창문이 모조리 깨져 나가며 수없이 많은 유리 조각이 바람에 휘감겼다.

단 한 번. 눈을 깜빡이기도 전에 거대한 바람은 내 코앞에 들이닥쳐 있었다.

- 인간!

스켈레톤 워로드가 인벤토리에서 내지르는 비명이 메아리처럼 울려 퍼졌다.

저놈은 자기 자신의 안위를 걱정하는 걸까, 아니면 날 걱정하는 걸까.

하긴, 둘 중 진짜 이유가 뭐건 간에 상관없다.

몇 분 전의 나와, 지금의 나는 큰 차이가 있으니까.

‘아.’

가슴 어림이 뜨겁게 달아올랐다. 무림인들이 단중혈(膻中穴), 혹은 중단전(中丹田)이라 불리는 그곳이 활짝 열렸다.

나를 둘러싼 모든 상황을 받아들여, 피부로 느끼고 눈으로 보게끔 만들었다.

‘그런 거였구나.’

세상이 느려지고, 모든 것이 선명하게 보이고 읽힌다.

칼날처럼 휘몰아치는 바람으로 이루어진 거대한 구. 그리고 그것을 가능케 만든 마력의 흐름이.

쉬쉬쉬쉬쉭!

모든 것에는 중심이 있는 법. 그것은 마법 역시 마찬가지다. 그리고 지금 내 눈에는 그 중심이 보였다.

‘지금.’

나는 느려진 세상 속에서 창을 휘둘렀다. 모든 것을 쓸어 버릴 것 같던 바람의 구가 백염의 창날을 따라 반으로 쪼개졌다.

거대한 하나에서 수백, 수천 개로 갈라진 바람의 칼날이 마력의 통제를 벗어나 좌우로 갈라져 사방을 찢었다.

서걱, 콰과과과과!

휘몰아치는 바람에 옷과 머리칼이 흩날렸다. 나는 희미한 미소를 띤 채 아크 리치를 올려다보았다.

“내려와. 목 아파.”

- 네놈……!

“싫으면, 내가 간다.”

콰지지직, 쾅!

단 한 번의 발 구름.

단단한 지면이 주저앉았고, 나는 잿빛 하늘을 향해 날아올랐다.



* * *



콰앙!

진태경이 지상으로부터 솟구친 그 순간, 아크 리치는 자신이 무엇을 해야 하는지 깨달았다.

‘저 인간이 다가오게 두어서는 안 된다.’

근접전을 피할 것. 마법사라면 누구나 알고 있는 사실이지만 아크 리치에게는 그 의미가 남달랐다.

‘이 몸이 한낱 인간 따위에게 위협을 느끼다니.’

이미 흑마법의 극의(極意)에 달했다고 자부하는 그였다.

비록 아크 리치로 부활하는 과정에서 상당한 힘을 잃어버렸지만, 그런 지금조차 대마도사를 한 수 아래로 보는 마력을 지녔다.

하지만 지금 자신을 향해 쏘아지는 저 인간은…… 위험하다.

‘그래, 마치 그때 그놈처럼.’

두 번 다시 떠올리기 싫은 기억이다. 아크 리치는 아직 썩지 않은 이를 악물며 마법을 펼쳤다.

- 그래비티(Gravity)!

지금까지와는 달리 힘이 실린 외침과 함께, 보이지 않는 무형의 중력이 반경 수십 미터를 짓눌렀다.

설령 S급 헌터라 해도 거스를 수 없는 압력이 진태경의 전신을 덮치려던 그 순간.

팡-!

진태경의 발끝에서 압축된 공기가 터져 나갔다. 허공답보(虛空踏步)로 중력 마법의 범위를 벗어난 신형이 재차 허공을 밟았다.

그가 보이는 표횰한 움직임은 한 마리의 매를 닮아 있었지만, 그 속도는 한낱 날짐승에 비할 바가 아니었다.

‘이 무슨.’

쾌속하게 허공을 누비며 다가오는 진태경의 모습에, 아크 리치의 안광이 깊게 가라앉았다.

지금 진태경은 중력 마법의 범위를 정확히 파악했을 뿐만 아니라, 기이한 수법으로 피하기까지 했다.

‘역시. 단순한 운으로 환영 마법을 파훼한 것이 아니다. 그렇다면…….’

후우우우웅!

아크 리치의 전신에서 흘러나온 마력이 공간을 뒤흔들었다.

- 그래비티. 그래비티. 그래비티.

어지간한 상급 마법사조차 한참 동안 스펠(Spell)을 읊어야 한다는 고위 마법이 쉴 새 없이 쏟아진다. 아크 리치는 이번에야말로 진태경을 떨어트릴 수 있을 거라 확신했다.

‘너, 인간이여. 추락하라.’

이번에는 중력 마법의 힘을 줄이는 대신 범위를 늘렸다. 반경 수백 미터를 짓누르는 중력을 어찌 피할 수 있…….

서걱!

아크 리치의 안광이 흔들렸다.

동시에 진태경을 짓누르려던 중력 마법이 흩어지고, 자신과 이어져 있던 마력이 실처럼 끊기는 것이 느껴졌다.

자신의 마법이 파훼 당했다는 사실에 순간 굳어 버린 아크 리치를 향해, 다시 한번 허공을 밟고 포탄처럼 쏘아진 진태경이 쇄도했다.

파앙! 쐐애애액!

파공성과 함께 아크 리치의 앞으로, 아니 그보다 한 걸음 위로 날아든 진태경이 백염을 내리그었다.

화륵, 푸른 불꽃의 선이 아크 리치를 향해 쏘아졌다.

콰창!

느려진 세상 속, 아크 리치를 둘러싼 무형의 방어막이 산산이 부서졌다.

삼 갑자의 열양지기를 장작 삼아 타오른 강기(罡氣)의 화염이, 수십 개로 중첩된 방어 마법을 깨트리고 아크 리치의 몸뚱어리를 향해 나아가던 그 순간이었다.

- 그레이트 본 월(Great Bone Wall)!

음산한 외침과 함께, 검은 뼈로 이루어진 장벽이 허공에서 솟구쳤다.

불과 1m의 거리를 두고 발현된 최상위 방어 마법과 화염을 머금은 창날이 부딪쳤다.

잿빛 하늘 위, 뼈의 장벽을 두고 마주한 두 사람을 중심으로 엄청난 충격파와 굉음이 천둥처럼 터져 나왔다.

꽈아아아아아앙!

응축된 바람이 터져 나갔다. 까마득한 상공을 맴돌던 구름이 흩어졌다. 간신히 형태를 유지하고 있던 건물이 붕괴하고, 반쯤 부패 된 시체가 바람에 휩쓸려 사라져 갔다.

하지만 이 모든 현상의 원인을 제공한 두 존재는 한 치의 흔들림도 없이 장벽 너머에 있을 서로를 바라보았다.

“아까웠다. 그치?”

- 그래, 제법이로구나. 아니…….

아크 리치가 장벽 중심을 관통한 투명한 창날을 바라보며 말을 이었다.

- 위험했다고 해 두지.

뼈의 장막을 통과한 창날의 길이는 손가락 한 마디 정도에 불과했지만, 순간 터져 나온 강기는 그의 코앞까지 들이닥쳤었다.

아크 리치에게는 다행스러운 일이었고, 진태경에게는 유감스러운 일이었다.

“운 좋다, 너.”

- 오만하구나. 인간이여. 하지만 인정하마.

“뭐?”

당황하는 진태경을 향해, 아크 리치가 천천히 말을 이었다.

- 너라면 그럴 만한 자격이 있다. 네가 진정 대적자라면 말이다.

“……대적자?”

- 그렇다. 왕의 대적자. 신의 농간으로 얽혀 있는 영원한 숙적이여. 아직 확신할 수는 없으나…… 내가 죽음의 강을 딛고 다시 일어설 수 있었던 이유도 그 때문이겠지.

진태경은 눈살을 찌푸렸다. 왕의 대적자는 무엇이고 신의 농간은 또 무슨 헛소리란 말인가.

“혹시 중2병이니? 이 뼈다귀 치우고 오른손 보여 줘 봐. 흑염룡 있나 보게.”

아크 리치는 고개를 저었다.

- 이것은 너와 나, 그 누구도 이해할 수 없는 일이다. 다만 한 가지는 확실하지.

갚게 가라앉아 있던 붉은 안광이 거세게 타올랐다.

처음에는 그저 강하고 별난 인간이라고 여겼으나, 지금은 아니다.

그는 수십 년 전, 왕을 보필하며 이 행성을 휩쓸던 기억을 떠올렸다.

모든 것을 잃고 죽음의 강으로 떨어지던 그 날, 처음이자 마지막으로 마주했던 한 인간의 모습도.

‘대적자.’

자신을 죽이고 왕마저 시해한 인간.

막으려 했으나 막을 수 없었고, 다가가려 했으나 범접할 수 없었던, 유일하게 그가 두려워했던 인간.

그리고 오늘, 아크 리치는 진태경과의 전투에서 그날의 기억을 떠올렸다.

- 넌…… 반드시 이 자리에서 죽는다.

음산하지만 그 어느 때보다 확고한 목소리가 울려 퍼졌다.

그리고 진태경의 대답은 간단했다.

“뭐래, 병신이.”

그리고 다음 순간.

“이거나 처먹어.”

화륵. 콰아아아!

나직한 목소리와 함께, 푸른 겁화가 실린 주먹이 막아서는 모든 것을 지우며 쏘아졌다.

검은 뼈로 이루어진 장막에 닿았다.

멸염신권(滅炎神拳).

콰드드드득!

어떤 공격도 막아낼 것 같던 뼈의 장막이 무너졌다.

산산이 비산하는 무수한 뼛조각들 너머로 보이는 아크 리치의 얼굴을 향해, 진태경이 무표정한 얼굴로 내뱉었다.

“이렇게 보니까 얼마나 좋냐. 목도 안 아프고.”

- ……!

“내려가.”

뻑!

빛살처럼 쏘아진 일권이, 아크 리치의 턱주가리를 후려쳤다.
```

## Final English reading copy

```markdown
# Chapter 422

*Ding. Ding. Ding.*

> **System**
>
> - There is always an opportunity in a crisis. You have gained a new insight in a battle where life and death hung in the balance!
>
> - **Middle Dantian** has been opened!
>
> - The opening of the **Middle Dantian** has increased all attributes by 20!
>
> - The effect of **circulating your qi** has greatly improved!
>
> - Your ability to perceive and control the flow of qi has greatly improved!
>
> - **Muscles and Bones** and **Sinews and Meridians** have increased!


The System notifications kept ringing in my ears without pause.

A breeze stirred my sweat-soaked hair, and I felt the new power and changes permeating my entire body.

Even the clear bell that rang at the very end.

*Ding.*

> **System**
>
> - As a reward for your enlightenment, you have gained a large amount of EXP!
>
> - As a reward for your enlightenment, you have gained 50 points!
>
> - Level Up!
>
> - As an effect of leveling up, all status ailments and fatigue have been cleared, and some injuries have healed!
>
> - The status effect **Curse** has been removed!
>
> - Your temporarily reduced attributes have returned to normal!

And I was not the only one who sensed these changes.

A master could not fail to know what his own hands had done. Realizing that his curse magic had been dispelled, the Arch Lich asked in a voice filled with disbelief,

“How in the world?”

I shrugged at the single word that encompassed every question it had.

“Well.”

“‘Well’?”

“Yeah. Well.”

“Do you think that explains anything?”

“Of course not. But why should I have to explain it to you?”

The emotion of sheer incredulity came across clearly in the Arch Lich’s faintly trembling eye-lights.

“You are clearly not a mage.”

“I wanted to be one. Their allowances are higher. But I had no talent. I wasn’t smart, either.”

“Even those humans you call archmages could not dispel my magic so easily.”

“They can’t. But it’s done.”

“What utter nonsense!”

I had to admit it.

The Arch Lich’s magic—no, its skill—was unquestionably superior to mine.

Even I, who had already far surpassed the limits of an ordinary Hunter, had been unable to avoid its curse magic. And the large-scale illusion magic using Bone Spears had been truly dangerous.

If I had not gained that insight, I might not even have been standing here now.

But…

“So what are you going to do about it?”

“……!”

I had the System, and I had merely done my best with the power and effort I had been given to overcome the crisis.

If it felt so unfair, it could use the System, too.

“That’s how the world works. Even if it feels like shit and pisses you off, you just have to put up with it and move on. What else can you do? It’s already happened. Right?”

The Skeleton Warlord, who had been screaming only moments ago, muttered,

“Wow. You sure know how to phrase things nicely.”

I could be like that sometimes.

“But, devious human, that one does not appear to have any intention of simply putting up with it and moving on.”

The Skeleton Warlord was right.

The next moment, an enormous vortex of mana formed, and an eerie voice rang out.

“Explode. Sonic Buster.”

And at the same time—

*Fwoooooosh! Boom!*

Highly compressed wind burst outward all at once.

Just brushing against the sphere of wind fired at the speed of sound was enough to pulverize concrete and snap steel reinforcing bars.

The windows of the high-rise buildings, unable to withstand the aftershock, shattered one after another, and countless shards of glass were swept up in the wind.

In a single instant—before I could even blink—the enormous mass of wind had reached the tip of my nose.

“Human!”

The Skeleton Warlord’s scream, hurled from inside my inventory, echoed like a cry from far away.

Was that bastard worried about its own safety, or mine?

It didn’t matter. Whatever the real reason was, it made no difference.

There was a world of difference between me a few minutes ago and me now.

*Ah.*

The area around my chest grew hot.

The spot martial artists called the Tanzhong acupoint, or the Middle Dantian, had opened wide.

It allowed me to take in everything surrounding me, feel it against my skin, and see it with my eyes.

*So that’s what it was.*

The world slowed down, and everything became clear enough to see and understand.

The enormous sphere made of wind whipping like blades.

And the flow of mana that made it possible.

*Shh-shh-shh-shh-shhk!*

Everything had a center. Magic was no exception.

And now, I could see that center.

*Now.*

I swung my spear through the slowed world.

The sphere of wind that looked as though it could sweep away everything in its path split in two along the blade of White Flame.

The wind blades that had split from one enormous whole into hundreds and thousands broke free of the mana controlling them, scattering left and right and tearing through everything around them.

*Shhk! Kwa-gwa-gwa-gwa!*

The raging wind whipped my clothes and hair around. With a faint smile on my lips, I looked up at the Arch Lich.

“Come down. My neck hurts.”

“You…!”

“Or I can come to you.”

*Crack-crackle! Boom!*

A single stomp.

The solid ground caved in, and I shot upward toward the ash-gray sky.

* * *
The instant Jin Taekyung shot up from the ground, the Arch Lich realized what it had to do.

*I must not let that human approach.*

Avoiding close combat was something every mage knew, but the meaning of it was different for the Arch Lich.

*This body is feeling threatened by a mere human.*

It prided itself on having already reached the pinnacle of dark magic.

Although it had lost a considerable amount of power during the process of being resurrected as an Arch Lich, even now it possessed enough mana to regard archmages as beings a level beneath it.

But the human flying toward it now…

*He is dangerous.*

*Yes, just like that bastard back then.*

It was a memory the Arch Lich never wanted to recall again. Clenching its still-intact teeth, it cast a spell.

“Gravity!”

Unlike before, the shout carried power. Invisible gravity pressed down over a radius of several dozen meters.

At the moment that pressure, impossible even for an S-rank Hunter to resist, was about to cover Jin Taekyung’s entire body—

*Pop!*

Compressed air burst from the tip of Jin Taekyung’s foot.

His body escaped the range of the gravity magic with *Stepping on Empty Air*, then stepped on the empty air again.

The nimble movements he displayed resembled those of a hawk, but his speed was beyond comparison with any mere flying creature.

*What is this?*

At the sight of Jin Taekyung racing through the air toward it, the Arch Lich’s eye-lights sank.

Jin Taekyung had not only precisely grasped the range of the gravity magic—he had even evaded it with some strange technique.

*As I thought. He did not dispel the illusion magic through mere luck. Then…*

*Whoooooooom!*

Mana flowed from the Arch Lich’s entire body and shook the surrounding space.

“Gravity. Gravity. Gravity.”

A high-level spell that even a fairly advanced mage would need to chant for quite some time poured out without pause.

The Arch Lich was certain that this time, it could knock Jin Taekyung down.

*You, human. Fall.*

This time, it reduced the power of its gravity magic in exchange for expanding its range.

How could Jin Taekyung possibly evade gravity pressing down over a radius of several hundred meters—

*Shhk!*

The Arch Lich’s eye-lights trembled.

At the same time, the gravity magic pressing down on Jin Taekyung scattered, and the mana connected to the Arch Lich was severed like a thread.

The Arch Lich froze for an instant at the fact that its magic had been dispelled.

Then Jin Taekyung stepped on the empty air once more and shot toward it like a cannon shell.

*Bang! Whoooosh!*

With a sharp crack through the air, Jin Taekyung flew before the Arch Lich—no, a step above it—and swung White Flame downward.

*Fwoom!*

A line of blue flame shot toward the Arch Lich.

*Crash!*

In the slowed world, the invisible barrier surrounding the Arch Lich shattered into pieces.

The flames of Force, fueled by three jiazi[^1] of Scorching Yang Qi, smashed through dozens of layered defensive spells and advanced toward the Arch Lich’s body.

[^1]: A jiazi is a traditional sixty-year cycle.

At that very moment—

“Great Bone Wall!”

With an eerie cry, a wall made of black bones rose from the air.

The highest-level defensive spell, manifested barely a meter away, collided with the flame-wreathed spearhead.

High above the ash-gray sky, an enormous shock wave and thunderous roar erupted around the two people facing each other with the bone wall between them.

*Kwaaang!*

Compressed wind burst outward.

The clouds circling far above scattered. Buildings that had barely maintained their shape collapsed, and half-rotted corpses were swept away by the wind.

Yet the two beings responsible for all those phenomena looked at each other beyond the barrier without so much as a tremor.

“That was close, wasn’t it?”

“Yes, quite impressive. No…”

The Arch Lich continued speaking as it stared at the transparent spearhead that had pierced through the center of the wall.

“I shall call it dangerous.”

The length of the spearhead that had passed through the bone barrier was no more than the width of a finger joint, but the Force that erupted in that instant had reached the tip of the Arch Lich’s nose.

For the Arch Lich, it had been a fortunate escape.

For Jin Taekyung, it had been unfortunate.

“You got lucky.”

“You are arrogant, human. But I will admit this much.”

“What?”

The Arch Lich slowly continued speaking toward the bewildered Jin Taekyung.

“You have earned the right to be so arrogant. If you truly are the Adversary.”

“……The Adversary?”

“That is right. The king’s Adversary. An eternal nemesis bound to him by a god’s machinations. I cannot be certain yet, but… that must also be why I was able to rise again after stepping into the River of Death.”

Jin Taekyung frowned.

What was the king’s Adversary? And what kind of nonsense was this about a god’s machinations?

“Are you suffering from middle-school syndrome? Get rid of those bones and show me your right hand. I want to see if you have a Black Flame Dragon.”

The Arch Lich shook its head.

“This is something that neither you nor I can understand. But one thing is certain.”

The deeply sunken red eye-lights flared fiercely.

At first, it had thought Jin Taekyung was merely a strong and unusual human.

But not anymore.

It recalled the memory of sweeping across this planet while serving the king decades ago.

It also recalled the figure of the human it had encountered on the day it lost everything and fell into the River of Death—the first and last time it had ever met that human.

*The Adversary.*

The human who had killed it and even assassinated the king.

The one it had tried to stop but could not, the one it had tried to approach but could not reach—the only human it had ever feared.

And today, in its battle with Jin Taekyung, the Arch Lich had remembered that day.

“You… will definitely die here.”

The eerie voice that rang out was more resolute than ever.

Jin Taekyung’s answer was simple.

“What the hell are you talking about, dumbass?”

And the next moment—

“Eat this, fucker.”

*Fwoom! Kwaaaaaa!*

Along with his low voice, a fist carrying blue hellfire shot forward, erasing everything that stood in its way.

It struck the curtain of black bones.

Flame-Extinguishing Divine Fist.

*Crack-crack-crack!*

The bone barrier that looked as though it could block any attack collapsed.

Beyond the countless fragments of bone scattering in every direction, the face of the Arch Lich came into view.

Jin Taekyung spoke with an expressionless face.

“See? Isn’t this much better? My neck doesn’t hurt, either.”

“……!”

“Down you go.”

*Wham!*

A single punch, fired like a ray of light, smashed into the Arch Lich’s jaw.
```
