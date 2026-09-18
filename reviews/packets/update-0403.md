<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0403.txt",
      "sha256": "33fed6b06fe9a3d14e6be54b10f2f0bdbb87df920d7d02bcf655ac5ff01ed76a",
      "bytes": 16372
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bc5e3a2cabb916daf7ce6c9c84853b1a69177276c1d83174065447d59d7628f3",
      "bytes": 1908
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1c37814ef5658d9022f66b3b32127bb21705dc26d6967091945cae0f256c3753",
      "bytes": 135760
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3980a63dfb7f4339af53ce24a5e793c4e2c22dd0154435139220c95f0ca5535b",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "24a09f9980e82c2c040c0eb51a35047027364e89a2533faf279b3aca529a07c9",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2ab9fdc5ac65ded492ae30563d08782589a0a2bfeffc1e31e6106629a95c3ade",
      "bytes": 622
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "e498b2e0cd4ef2ddd958a76d0407075f9ca628d8106cd482eba8daa67496182c",
      "bytes": 893
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "ebd736367f1d2664cd14d1e735ced05239a631da61b9b53b19caad2517b01ce4",
      "bytes": 555
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "12cfb4c08ca1583146125841018dec5aacd756fbf22d01abba18bbe2b7ecaec0",
      "bytes": 117907
    }
  ],
  "estimated_tokens": 11457
}
-->

# Durable State Update — Chapter 403

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 403. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 403. Profile updates may replace only one
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
  "chapter": 403,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 403,
    "continuity_sources": [403],
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
    "The black knight was Lei Fei, whose human identity and memories were restored when Jin told him to rest.",
    "Lei Fei was raised by Wei Fenghu, whom he regarded as both uncle and father, and his human memories include his wife and daughter.",
    "Lei Fei was a level-120 undead Death Knight Lord when his identity returned, but his body was already collapsing.",
    "Lei Fei's undead service and slaughter of humans were caused by the Arch Lich's control rather than his own will.",
    "Lei Fei reaffirmed his Hunter oath and fought one final battle beside Jin.",
    "Lei Fei raised the fallen Public Security Armed Forces Department Hunters as undead for the final battle.",
    "Jin and Lei Fei's forces destroyed the remaining monster army, after which the undead Hunters collapsed.",
    "Lei Fei died and scattered into dust after asking Jin to send his love and apology to his family.",
    "Lei Fei's final instruction to Jin was to go west and end the war.",
    "Dozens of aircraft arrived over the battlefield after Lei Fei's death."
  ],
  "continuity_sources": [
    402,
    401
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to Lei Fei's wife and daughter during the Gaoping District Monster Wave?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What awaits Jin to the west, and how can the ongoing war be ended?"
  ],
  "safe_through": 402,
  "temporary_decisions": [
    "Render 나이트메어 as Nightmare.",
    "Use black knight for 검은 기사 and keep it distinct from Death Knight and Death Knight Lord.",
    "Render 언령 as word-spell.",
    "Render 중화 육성 훈련 as Zhonghua Development Training.",
    "Preserve Jin's blunt, profane combat voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 평화 | **Peace Guild** | Guild name. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 인민해방군 | **People's Liberation Army** | Chinese military deployed to seal off the catastrophe area. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 레이페이 | 웨이펑후 | nephew_to_maternal_uncle_and_adoptive_father | Uncle; later Father | childlike-familiar | Lei Fei calls Wei Fenghu his uncle and later acknowledges him as his father. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 402
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 402
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 402
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 402
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 401
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son, and he has asked Jin Taekyung to bring Lei Fei back if he is found.

## Korean source

```text
＃403화



이십여 대의 군용 수송기와 호위를 위해 따라붙은 전투기들은 착륙부터 난항을 겪었다.

「이, 이런.」

「착륙 지점을 찾을 수 없습니다!」

온통 폐허가 된 소도시.

빼곡하게 들어찬 건축물들은 도미노처럼 쓰러져 있고, 곳곳에서는 화염이 솟구쳤다.

하지만 무엇보다 파일럿들을 두렵게 만든 것은, 까마득한 상공에서도 내려다보이는 참혹한 광경이었다.

학교 운동장, 편의점, 관공서…… 평화로운 일상이 사라진 그곳에는 시체의 산과 붉은 핏물의 강이 빈자리를 채우고 있었다.

몬스터 군단이 그려 낸 한 폭의 지옥도(地獄道).

생명이라고는 존재하지 않는 지상을 바라본 이들이 형용할 수 없는 공포에 몸을 떨던 그때였다.

「착륙하게.」

「초, 총사령관님. 하지만…….」

「하지만이 아니라 반드시, 일세. 이건 명령이야.」

묵직한 음성을 토해 낸 장년인의 굳은 얼굴을 마주한 파일럿은 선택의 여지가 없음을 깨달았다.

자신은 군인이었고, 상대는 이번 전쟁을 지휘하는 실질적인 총사령관이었으니까.

샤오 주석의 신임을 한몸에 받는 심복이자, 중앙 군사위원회 국방부장인 웨이펑후 상장의 명령에 불복하는 건 미친 짓이었다.

그리고 다음 순간 이어진 웨이펑후의 한마디에, 파일럿은 생각했다.

차라리 명령 불복종이 덜 미친 짓일 거라고.

「서부 전선이 임시 본부로 삼은 종합병원으로 가게.」

「예? 하지만 그곳은…….」

「마지막으로 도착한 통신에 의하면 가장 치열한 격전이 벌어진 곳이겠지. 어쩌면 지금까지도. 나 역시 잘 알고 있네.」

「…….」

「어쩌면 이미 늦었을지도 모르네. 그러나 우린 가야 해. 아직 한 사람이라도 살아 있다면 그를 도와 싸워야지.」

깊게 가라앉은 눈빛을 한 웨이펑후가 말을 이었다.

「조종간을 잡게. 그리고 가장 먼저 착륙하게.」

총사령관인 그가 직접 여기까지 온 것도 파격적인 일인데, 가장 먼저 착륙을 시도하라니. 아직 남아 있을 몬스터들을 생각하면 그야말로 엄청난 위험을 동반하는 일이다.

‘빌어먹을.’

눈을 질끈 감은 파일럿은 통신을 켰다. 이내 잘게 떨리는 목소리가 통신망을 타고 전 기체에 퍼져 나가기 시작했다.

「VIP-777이 전 기체에 명령한다. 전 기체에 명령한다…….」

자신의 명령이 하달되는 것을 들으며, 웨이펑후는 천천히 심호흡했다.

만일의 사태를 대비해 몸에 걸친 낙하 장비가 천근 바위처럼 무겁게 느껴졌다.

‘삼십여 년 만의 실전이라 그런가. 떨리는군.’

그리고 이런 감정은 비단 웨이펑후 혼자만의 것이 아니었다.

이십여 기의 군용 수송기에 몸을 실은 4천 명의 헌터 모두가 크고 작은 두려움을 품고 있었다.

누군가는 당장이라도 도망치고 싶을 것이고, 누군가는 두려움을 억누르며 애써 전의를 불태우고 있을 것이다.

곧 시작될 전투에서 누가 죽을지는 아무도 알 수 없다. 웨이펑후 역시 예외는 아니며, 총사령관인 그가 위험을 무릅쓰고 격전지에 온 것은 병사들의 사기 때문이었다.

‘부하들만 사지로 몰아넣는다면 지휘관의 자격이 없다.’

그것이 웨이펑후의 평생 지론이었고 친아들이나 다름없는 외조카, 레이페이는 그런 숙부를 존경했다.

문득 눈앞을 스치는 그리운 얼굴에 늙은 장군의 가슴 한구석이 욱신거렸다.

「……보고 싶구나.」

웨이펑후는 작게 중얼거렸다.

레이페이가 실종된 지 어느덧 보름. 하지만 그는 희망의 끈을 놓지 않았다. 안전한 곳으로 옮겨진 레이페이의 아내와 딸 역시 마찬가지였다.

‘나는 오늘, 널 닮은 이를 보았다.’

아직 이십 대에 불과한 젊은이. 머나먼 타지에서 엄청난 전공을 쌓은 그는 서부 전선이 위험에 빠졌다는 소식에 망설임 없이 떠났다.

심지어 생존확률 10%에 불과한 텔레포트를 시도하며 웃었다고 했다.



‘괜찮네요. 10% 정도면.’

‘아마도, 차원을 넘을 확률보다는 천 배 정도 높을 테니까.’



매직 존슨으로부터 그 소식을 전해 들었을 때, 웨이펑후는 즉시 총사령부의 전력을 동원해 편대를 꾸렸다.

외국인에 불과한 청년, 진태경이 보여 준 기개에 충격을 받았고 그런 그의 모습에서 실종된 외조카를 떠올렸다.

‘너 역시 그리했겠지. 그렇지 않으냐?’

들리지 않는 물음을 던진 웨이펑후의 입가에 희미한 미소가 맺힌 바로 그 순간이었다.

「이, 이럴 수가……!」

「초, 총사령관님!」

파일럿들의 다급한 외침에 고개를 내민 웨이펑후의 시선이 창밖을 향했다.

서서히 가까워지는 지상, 그곳에는 지금껏 목격한 어느 전장보다 참혹한 시산혈해(屍山血海)가 펼쳐져 있었다.

시체와 피, 피와 시체…….

서부 전선의 임시 사령부인 종합병원은 처참히 무너져 흉한 철골을 드러냈고, 지옥의 입구처럼 뻥 뚫린 거대한 싱크홀(Sinkhole)과 지면에 아로새겨진 수십 개의 크레이터에는 적녹색의 핏물이 가득 채워져 있었다.

뒤섞여 쓰러진 몬스터와 인간의 시체는 헤아릴 수도 없이 많았다. 수천? 아니, 일만을 훌쩍 넘겼다.

「……맙소사.」

「도, 도대체 누가?」

재앙이 할퀴고 지나간 죽음의 땅.

할 말을 잃고 처참한 지상을 바라보던 파일럿들은 웨이펑후의 외침에 퍼뜩 정신을 차렸다.

「고도를 낮추게, 어서!」

「예, 옛!」

몬스터에 대한 위협은 사라졌지만 방심해서는 안 된다.

파일럿은 어느 때보다 신중하게 기체를 조종했고, 식은땀으로 몸이 흠뻑 젖은 상태로 착륙을 시도했다.

키기기기긱, 쿠쿵!

수차례의 격한 진동이 휩쓸고 지나간 기체. 마침내 착륙에 성공한 수송기에서 가장 먼저 내린 사람은 다름 아닌 웨이펑후였다.

타다다닥!

그의 뒤를 따라 수송기에 탑승해 있던 이백여 명의 헌터들이 신속히 지상에 발을 디뎠다.

그리고 그들이 보인 반응은 두 가지로 나뉘었다.

「이런 미친…….」

상상치도 못한 광경에 대한 경악.

「우욱, 우웨에에엑!」

주위를 가득 메운 피비린내와 조각난 시신들로부터 느끼는 욕지기.

동시에 뇌리를 가득 채운 의문.

‘도대체 누가?’

생존자를 찾아야 한다는 것도 잊은 채, 웨이펑후를 비롯한 모든 이들이 석상처럼 굳어 버린 바로 그 순간이었다.

철벅, 철벅.

고요한 전장에 울려 퍼지는 발걸음 소리.

바닥에 고인 핏물을 밟으며 전장을 가로지르는 한 사람을 향해 이백여 쌍의 시선이 몰려들었다.

머리부터 발끝까지, 온통 녹색 피를 뒤집어쓴 그를 바라보던 웨이펑후가 신음처럼 중얼거렸다.

「진 선생……?」

분명 그였다.

혈인(血人)이나 다름없는 모습이었지만 웨이펑후는 알아볼 수 있었다.

생존확률 10%의 텔레포트 마법, 암담한 전황을 뒤집고 진태경은 살아남았다.

멈추지 않을 것 같던 그의 걸음이 웨이펑후의 앞에서 정지했다.

철벅.

몬스터의 끈적한 핏물로 엉겨 붙은 머리카락을 쓸어올린 진태경은, 침묵 끝에 첫 마디를 뗐다.

“전투는 끝났습니다. 살아남은 몬스터는…… 없습니다.”

「……!」

「……!」

믿을 수 없는 그의 한마디에, 좌중은 전율에 휩싸였다.

서부 전선에서 보내온 마지막 통신에 의하면 몬스터 군단의 숫자는 자그마치 일만에 달했다.

그뿐만이 아니다. 아크 리치의 심복으로 여겨지는 데스나이트 로드가 직접 나섰으니 다섯 개 전선 중 가장 압도적인 공세였다.

반면 그에 맞서 싸운 헌터의 숫자는 고작 천여 명. 그 외의 인민해방군은 종잇조각이나 다름없었다.

‘그런 전투에서 이긴 것으로도 모자라, 일만의 몬스터 군단을 전멸시키다니.’

한 사람이 없었다면 불가능했을 전투. 동시에 한 사람이 있었기에 가능했던 승리.

S급 헌터가 단번에 전황을 뒤집을 수 있는 전략 병기라지만, 대격변 이래 그 누가 이런 업적을 세웠던가.

이백여 명의 헌터는 경외(敬畏) 어린 시선으로 눈앞의 청년을 바라보았다.

그러나 한 사람, 웨이펑후만큼은 달랐다.

늙은 장군은 슬픔과 두려움이 담긴 눈빛으로 진태경을 응시했다. 아니, 그의 손에 들린 한 자루 검을 바라보고 있었다.

더 없이 눈에 익은 검이었고, 그래서 더 가슴이 아팠다.

지금의 상황이 무엇을 뜻하는지 알기에.

「그 아이를…… 만났소?」

잠시 침묵하던 진태경이 대답했다.

“사랑한다고 전해 달라더군요.”

「……!」

“미안하다고도 했습니다.”

웨이펑후는 새어 나오는 울음을 참으려 이를 악물었다. 희뿌옇게 물드는 시야 속에서, 마지막 한마디가 귓가에 닿았다.

“제가 본 최고의 헌터였습니다.”

거기까지였다. 투툭, 웨이펑후의 주름진 피부 위로 눈물이 흘러내렸다.

어디선가 불어온 바람이 그를 부드럽게 감싸 안았다.



* * *



등급이나 업적, 헌터냐 아니냐는 중요하지 않다.

다른 사람의 위해 스스로를 희생했다는 것만으로도 그는 영웅이라 불릴 자격이 충분하니까.

그렇기에 레이페이는 내 기억에 오래도록 남아 있을 것이다.

언데드로 부활했으나 인간으로 죽은 자.

마지막까지 사명을 다한 그야말로 진정한 헌터고, 영웅이다.

오늘 이 자리에서 죽어 간 수많은 이들 역시 마찬가지였다.

그리고…… 아직 의식을 회복하지 못한 두 사람도.

‘피로가 모두 회복되기 전까지는 깨어나지 않을 거라고 했었지.’

앞서 다녀간 힐러가 해 준 말을 떠올리며, 깊은 잠에 빠진 최 팀장과 샤오 쉔을 바라봤다.

최상급 포션 덕분에 두 사람의 부상은 씻은 듯이 나았지만, 신체와 정신에 누적된 피로는 별개의 문제다.

‘레벨 업을 하는 나조차도 가끔은 기절하니까.’

두 사람은 마지막까지 용감하게 싸웠다.

사지가 잘려 나가는 고통 속에서도 손에 쥔 무기를 놓지 않을 만큼.

“영웅, 영웅이라…….”

낮게 뇌까린 나는 옆에 놓아둔 검을 바라보았다. 바로 그 영웅이 남긴 검이자 유품.

하염없이 눈물을 흘리던 웨이펑후는 극구 사양하는 내게 그 검을 돌려주며 말했다.



‘그 녀석도 진 선생이 맡아 주길 원했을 거요.’



정말입니까, 레이페이?

답이 돌아오지 않을 질문을 던지며 검신을 매만졌다. 보는 것만으로도 서늘한 예기(銳氣)가 느껴지는 명검이다.

‘아이템 감정.’

띠링.



아이템창



[영웅의 혼]

종류 : 검

등급 : 초절정

제한 : 영웅에 부합하는 자

설명 : 극도로 단단하며 날카롭다. 숭고한 영웅의 마지막 혼이 서려 있으며, 자격에 부합하는 자는 더욱 강한 힘을 낼 수 있다.





영웅의 혼?

레이페이를 생각하니 어울리는 이름이지만, 확실히 묘한 검이었다.

치열한 공방 속에서도 실금 하나 가지 않았으니 초절정의 등급은 그렇다 치고, 제한부터가 독특했다.

‘올바른 심성을 지닌 자만 사용할 수 있다고?’

음. 어디 한번 시험해 볼까.

망설임 없이 검 자루를 쥔 나는 허공을 향해 내리그었다.

쉬익!

생각보다 좋다.

무게와 균형감도 딱 알맞고, 바람조차 갈라 버리는 예리함도 마음에 들었다. 곧장 들려온 시스템 알림까지 더해지니 금상첨화다.

띠링.



- [영웅의 혼]이 당신을 올바른 심성의 소유자로 인식했습니다.

- [영웅의 힘]이 발현되었습니다. 모든 능력치가 미약하게 상승하고 피로감이 줄어듭니다. 특정 상황에 따라 더욱 큰 힘을 끌어낼 수 있습니다.



그 특정 상황이 뭔지는 모르겠지만 지금은 아닌 모양이다. 올랐다는 능력치도 정말 쥐꼬리만큼이라 느껴지지도 않았다. 마치 호숫가에 물 한 바가지 더 넣은 기분이랄까.

‘대신 인성 평가용으로는 딱 맞겠는데.’

이름하여, 인성 판별 검.

앞으로 접근하는 놈들은 영웅의 혼으로 테스트해 볼 생각이다. 검이 받아들일 정도로 올바른 놈이라면 가깝게 지내고, 아니면 삭초제근(削草除根)한다는 마음가짐으로 쓱싹…….

파지직!

순간 손아귀를 타고 흐르는 강한 전류에 나는 검을 놓쳐 버렸다.

“뭐야, 이거?”

황당함이 밀려드는 가운데, 날카로운 알림과 함께 시스템 메시지가 허공에 떠올랐다.

삐빅!



- 당신은 악한 마음을 품었습니다!

- [영웅의 혼]이 당신을 거부했습니다!

- [영웅의 힘]의 효과가 사라집니다!



“…….”

어이없네. 그냥 해 본 생각이었는데.

떨어진 검을 내려다보던 나는 피식 웃어 버렸다. 어쩌면 레이페이의 혼이 조금은 깃들었을지도 모르겠다는 생각이 문득 들었다.

잠깐, 그렇다면?

“듣고 있냐?”

잠깐의 침묵이 흐른 뒤, 인벤토리에 넣어 둔 스켈레톤 워로드가 대답했다.

- ……그렇다.

“다른 게 아니라, 한 가지 물어볼 게 있어서.”

- ……혹시 그 질문이 에고 소드(Ego Sword)에 관한 것이라면 아니라고 대답해 주지. 저 검에는 아주 미약한 영혼의 흔적만이 남아 있을 뿐, 네가 생각하는 그 인간은 이미 소멸했다.

평소에는 나사 빠진 놈이지만 명색이 네임드 몬스터이자 망자 군단의 사령관이다.

레이페이의 소멸 당시 흩어지는 마력을 일부 흡수하여 더욱 강해졌으니, 녀석의 말은 사실일 가능성이 높았다.

그건 그렇고…….

“무슨 일 있냐?”

- 음?

“그냥, 아까부터 분위기가 음울하길래.”

말해 놓고도 이게 말이 되나 싶다. 언데드 몬스터에게 왜 분위기가 음울하냐니. 원래 태생부터 음울한 놈들 아닌가.

‘안 하던 놈이 이러니 문제지.’

그런데 그때 스켈레톤 워로드가 불쑥 입을 열었다.

- 문득 그런 생각이 들었다.

“무슨 생각?”

- 과거의 나는, 어떤 존재였을까.

“……!”

- 내게는 아무런 기억도 존재하지 않는다. 레이페이라는 인간은 비록 소멸했지만, 본 사령관은 내심 그가 부러웠다. 적어도 자신이 누구인지는 알게 되었으니.

녀석이 이런 생각을 하고 있을 줄이야.

잠시 고민하던 나는 따뜻한 목소리로 말을 건넸다.

“그럼 소멸시켜 줄까?”

- ……!

“왜, 부러웠다며.”

- 아, 아니, 내 말은 그런 게 아니고…….

스켈레톤 워로드의 다급한 변명은 끝까지 이어지지 못했다. 노크와 함께 문 너머에서 들려온 정중한 목소리 때문이었다.

「진 선생님. 국무부장 동지께서 찾으십니다.」

벌써 시간이 된 모양이다.

“네. 지금 갈게요.”

나는 잠에 빠져 있는 두 사람을 마지막으로 바라본 뒤 자리에서 일어섰다. 그리고 미처 해 주지 못한 말을 중얼거렸다.

“글쎄, 아마도 내 생각에는 썩 괜찮은 놈이었을 것 같은데.”

- ……어? 혹시 그거 본 사령관에게 한 말인가?

“아니. 그냥 혼잣말인데.”

- 커, 커흠. 그렇지?

하지만 풀이 잔뜩 죽어 있던 스켈레톤의 목소리가 밝아진 것은, 결코 착각이 아닐 거다. 나는 실소를 흘리며 방을 나섰다.
```

## Final English reading copy

```markdown
# Chapter 403

The twenty-some military transport aircraft and their fighter escorts had trouble landing from the moment they arrived.

“W-What the……”

“We can’t find a place to land!”

Below them lay a small city that had been reduced entirely to ruins.

The buildings packed tightly together had collapsed like dominoes, and flames rose from here and there.

But what frightened the pilots more than anything was the horrific sight visible even from high above.

Schoolyards, convenience stores, government offices……

In that place, where peaceful daily life had vanished, mountains of corpses and rivers of red blood filled every empty space.

A hellscape painted by the monster army.

As the pilots trembled with indescribable terror while looking down at the lifeless ground, a voice rang out.

“Land.”

“C-Commander-in-Chief, but……”

“Not ‘but.’ You must land. That is an order.”

When the pilot met the hardened face of the middle-aged man who had spoken in a heavy voice, he realized he had no choice.

He was a soldier, and the man before him was the de facto commander-in-chief directing this war.

Disobeying the order of General Wei Fenghu, the Minister of National Defense under the Central Military Commission and Chairman Xiao’s most trusted subordinate, would have been insane.

Then Wei Fenghu spoke again, and the pilot thought that disobeying the order might actually be less insane.

“Go to the general hospital the Western Front has been using as its temporary headquarters.”

“What? But that place……”

“According to the last communication we received, that is where the fiercest battle took place. Perhaps it is still going on.”

“……”

“I know that as well as you do. We may already be too late. But we have to go. If even one person is still alive, we must help them and fight alongside them.”

Wei Fenghu continued, his gaze sunk deep.

“Take the controls. And land first.”

It was extraordinary enough that the commander-in-chief had come all the way here himself. But ordering them to attempt the first landing was something else entirely. Considering that monsters might still remain, it was a decision accompanied by tremendous danger.

*Damn it.*

The pilot squeezed his eyes shut and turned on the radio. Soon, his trembling voice began to spread through the communications network to every aircraft.

“VIP-777 issuing orders to all aircraft. I repeat, orders to all aircraft……”

As he listened to his orders being relayed, Wei Fenghu slowly drew a deep breath.

The parachute equipment he had put on in case of an emergency felt as heavy as a thousand-pound boulder.

*Is this because it’s been more than thirty years since I last saw real combat? I’m trembling.*

And Wei Fenghu was not the only one feeling that way.

All four thousand Hunters aboard the twenty-some military transports carried fears large and small.

Some probably wanted to run away right then and there. Others were suppressing their fear and desperately trying to fan their fighting spirit.

No one knew who would die in the battle that was about to begin. Wei Fenghu was no exception, and the reason the commander-in-chief had come to the battlefield despite the danger was the morale of his soldiers.

*A commander has no right to drive only his subordinates into a place of death.*

That had been Wei Fenghu’s lifelong principle, and his nephew through his sister—who was like a biological son to him—Lei Fei had respected him for it.

At the sudden memory of a beloved face passing before his eyes, a corner of the old general’s heart ached.

“I miss you.”

Wei Fenghu murmured quietly.

It had already been fifteen days since Lei Fei had gone missing. But he had not let go of hope. Neither had Lei Fei’s wife and daughter, who had been moved to a safe place.

*Today, I saw someone who reminded me of you.*

A young man who was still only in his twenties. He had achieved an incredible military feat in a distant foreign land, and when he heard that the Western Front was in danger, he had left without hesitation.

He had even laughed while attempting a teleport with a survival rate of only ten percent.

*“Ten percent sounds pretty good.”*

*“It’s probably a thousand times more likely than crossing dimensions.”*

When Magic Johnson relayed that news to him, Wei Fenghu had immediately mobilized the headquarters’ forces and organized the squadron.

He had been struck by the courage shown by a young foreigner named Jin Taekyung, and seeing him had reminded Wei Fenghu of his missing nephew.

*You would have done the same, wouldn’t you?*

Just as Wei Fenghu’s lips curved into a faint smile after asking the silent question, a cry rang out.

“H-How can this be……”

“C-Commander-in-Chief!”

Wei Fenghu raised his head at the pilots’ urgent shouts and looked out the window.

The ground was gradually drawing closer. Across it lay a sea of corpses and blood more horrific than any battlefield he had ever witnessed.

Corpses and blood, blood and corpses……

The general hospital serving as the Western Front’s temporary headquarters had collapsed miserably, exposing its ugly steel framework. A gigantic sinkhole, gaping open like the entrance to hell, and dozens of craters carved into the ground were filled with red and green blood.

There were more monster and human corpses than anyone could count, sprawled together in tangled heaps.

Thousands?

No, well over ten thousand.

“My God……”

“W-Who did this?”

A land of death, raked by disaster.

The pilots, speechless as they stared at the devastated ground, abruptly came to their senses when Wei Fenghu shouted.

“Lower our altitude! Quickly!”

“Yes, sir!”

The threat from the monsters had vanished, but they could not afford to let their guard down.

The pilot maneuvered the aircraft more carefully than ever and attempted to land with his entire body drenched in cold sweat.

Krrrrrrk, boom!

The aircraft shuddered violently several times. At last, when the transport successfully landed, the first person to step out was none other than Wei Fenghu.

Rapid footsteps followed.

The two hundred Hunters aboard the transport quickly set foot on the ground behind him.

Their reactions split into two kinds.

“This is fucking insane……”

Shock at a sight beyond anything they could have imagined.

“Urk, urrrrgh!”

Nausea at the stench of blood filling the surroundings and the dismembered corpses.

At the same time, one question filled every mind.

*Who did this?*

They had even forgotten that they needed to search for survivors. Wei Fenghu and everyone else stood frozen like stone statues.

Then—

Splash. Splash.

Footsteps echoed across the silent battlefield.

Two hundred pairs of eyes turned toward a single person crossing the battlefield, stepping through the pools of blood covering the ground.

The man was drenched in green blood from head to toe. Wei Fenghu stared at him and muttered as if groaning.

“Mr. Jin……?”

It was definitely him.

Even though he looked no different from a man made entirely of blood, Wei Fenghu recognized him.

Jin Taekyung had survived a teleportation spell with a ten-percent survival rate, overturned the hopeless course of the battle, and lived.

The footsteps that seemed as though they would never stop came to a halt in front of Wei Fenghu.

Splash.

Jin Taekyung brushed back the hair clotted together with the monsters’ sticky blood. After a long silence, he spoke his first words.

“The battle is over. There are… no monsters left alive.”

“……!”

“……!”

His unbelievable statement sent a shudder through everyone present.

According to the last communication sent from the Western Front, the monster army had numbered no fewer than ten thousand.

And that was not all. A Death Knight Lord believed to be one of the Arch Lich’s trusted servants had personally entered the battle, making it the most overwhelming offensive of the five fronts.

By contrast, barely a thousand Hunters had fought against them. The rest of the People’s Liberation Army had been no more useful than scraps of paper.

*Not only did he win that battle—he annihilated a monster army of ten thousand.*

It was a battle that would have been impossible without one person. And at the same time, a victory that had been possible because one person was there.

An S-rank Hunter was said to be a strategic weapon capable of overturning a battlefield in an instant. But since the Great Cataclysm, who had ever accomplished something like this?

The two hundred Hunters looked at the young man before them with reverence.

But Wei Fenghu was different.

The old general stared at Jin Taekyung with grief and fear in his eyes.

No—not at Jin Taekyung himself.

At the sword in his hand.

It was a sword Wei Fenghu knew far too well, and that was why his heart hurt even more.

He knew what the situation meant.

“Did you…… meet him?”

After a brief silence, Jin Taekyung answered.

“He asked me to pass along his love.”

“……!”

“He also said he was sorry.”

Wei Fenghu clenched his teeth to hold back the sob rising from his throat. Through his vision clouding with tears, he heard one final sentence.

“He was the best Hunter I’ve ever seen.”

That was all.

Tears trickled down Wei Fenghu’s wrinkled face.

A breeze blew from somewhere and gently wrapped around him.

* * *

Rank, achievements, whether someone was a Hunter or not—it did not matter.

The fact that he had sacrificed himself for someone else was enough to make him worthy of being called a hero.

That was why Lei Fei would remain in my memories for a long time.

A man who had been resurrected as an undead but died as a human.

A true Hunter and hero who fulfilled his mission to the very end.

The countless others who had died here today were the same.

And so were the two people who had not yet regained consciousness.

*The healer said they wouldn’t wake until they had recovered from all their fatigue.*

I looked at Team Leader Choi and Shao Shen, both lost in a deep sleep, remembering what the healer who had visited earlier had said.

Thanks to the top-grade potion, both of their injuries had healed as if they had never existed. But the fatigue accumulated in their bodies and minds was another matter.

*Even I occasionally pass out, and I level up.*

The two of them had fought bravely to the very end.

They had held on to their weapons even while enduring the pain of having their limbs severed.

“Heroes…… heroes, huh.”

I muttered the word under my breath and looked at the sword lying beside me.

The sword left behind by that very hero. His keepsake.

Wei Fenghu had wept endlessly as he returned the sword to me despite my repeated refusal.

*“He would have wanted you to keep it too, Mr. Jin.”*

*Really, Lei Fei?*

I ran my fingers over the blade as I asked a question that would never receive an answer.

It was an exceptional sword whose chilling edge could be felt simply by looking at it.

*Item appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Hero’s Soul**
>
> **Type:** Sword  
> **Grade:** Supreme Peak  
> **Restriction:** Those worthy of being called heroes  
> **Description:** Extremely hard and sharp. The final soul of a noble hero dwells within it, and those who meet its qualifications can draw out even greater power.

*Hero’s Soul?*

It was a fitting name for Lei Fei, but the sword was certainly strange.

The Supreme Peak Grade made sense, considering that it had not suffered even a hairline crack amid such fierce exchanges. But the restriction was unusual from the start.

*Only someone with an upright character can use it?*

Hmm. Why not put it to the test?

Without hesitation, I gripped the hilt and slashed downward through the air.

Whoosh!

Better than I expected.

The weight and balance were just right, and I liked the sharpness that could even cut through the wind. The System notification that came immediately afterward was the icing on the cake.

Ding.

> **System**
>
> - **Hero’s Soul** has recognized you as someone of upright character.
> - **Hero’s Power** has manifested. All stats have increased slightly, and fatigue has been reduced. You may draw out even greater power depending on the situation.

I had no idea what that specific situation was, but apparently this was not it. The increase in my stats was so tiny that I could not feel it at all.

It was like pouring one more bucket of water into a lake.

*Still, it would be perfect for evaluating someone’s character.*

A sword for judging character.

From now on, I planned to test anyone who approached me with Hero’s Soul. If the sword accepted them, I would stay close to them. If not, I’d cut the weeds out by the roots and—snip…

Crackle!

A powerful electric current suddenly ran through my hand, and I dropped the sword.

“What the hell?”

As bewilderment washed over me, a sharp alarm rang out and a System message appeared in the air.

Beep!

> **System**
>
> - You have harbored an evil intention!
> - **Hero’s Soul** has rejected you!
> - The effect of **Hero’s Power** has disappeared!

“……”

Come on. It was just a passing thought.

I looked down at the fallen sword and let out a quiet laugh. For some reason, it suddenly occurred to me that perhaps a little of Lei Fei’s soul had entered it.

Wait. If that was true……

“Are you listening?”

After a brief silence, the Skeleton Warlord, who had been placed inside my inventory, answered.

—……I am.

“I wanted to ask you something.”

—……If that question concerns the ego sword, I will answer no. Only the faintest trace of a soul remains within that sword. The human you have in mind has already ceased to exist.

He usually had a screw loose, but he was still a named monster and commander of the army of the dead.

He had absorbed some of the mana scattered when Lei Fei disappeared and grown even stronger, so there was a good chance his words were true.

That aside……

“Is something wrong?”

—Hmm?

“You’ve seemed gloomy for a while.”

Even after saying it, I wondered whether that made any sense. Why was I asking an undead monster why he seemed gloomy? Weren’t they gloomy by nature?

*That’s the problem—he wasn’t acting like this before.*

But then the Skeleton Warlord suddenly spoke.

—A thought occurred to me.

“What thought?”

—What kind of being was I in the past?

“……!”

—I have no memories at all. Although the human named Lei Fei has ceased to exist, this commander was secretly envious of him. At least he learned who he was.

I had not expected him to be thinking about something like that.

After considering it for a moment, I spoke in a warm voice.

“Then should I make you cease to exist too?”

—……!

“What? You said you were envious.”

—N-No, that’s not what I meant……

The Skeleton Warlord’s frantic excuse did not reach its end.

A knock sounded, followed by a polite voice from beyond the door.

“Mr. Jin. Comrade Minister of State would like to see you.”

It seemed the time had already come.

“Yes. I’ll be right there.”

I took one last look at the two people sleeping soundly, then rose from my seat. As I did, I muttered the words I had not managed to say earlier.

“Well, in my opinion, you were probably a pretty decent guy.”

—……Huh? Were you talking to this commander?

“No. I was just talking to myself.”

—Ahem. Right?

The Skeleton’s voice had been utterly dejected until then, but it brightened.

That was definitely not my imagination.

I let out a quiet laugh and left the room.
```
