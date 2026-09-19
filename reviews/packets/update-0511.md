<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0511.txt",
      "sha256": "fdce6533c29b62a716ee640b2bacd5395229841cdf98603ae57df8e1b54bd5bc",
      "bytes": 12846
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "328abd7f598a31dad15be43143bca0f1195f5ce937ad411a58b224ccd8f85a9b",
      "bytes": 4015
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "73c9d885c23e8ca6b2a0ed4668e32bb7c10761c39bc7cd0aac80b8f93e0206d1",
      "bytes": 163106
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "034317e849b114422ee116c5a41333d43942e4e85bb5b54e47c55a05b4c5d1c3",
      "bytes": 553
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55e1b559aab842913d6859ee4f86aff71a3a23ad89553d949f27b82a0965ae8",
      "bytes": 154523
    }
  ],
  "estimated_tokens": 9004
}
-->

# Durable State Update — Chapter 511

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 511. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 511. Profile updates may replace only one
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
  "chapter": 511,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 511,
    "continuity_sources": [511],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun and the New Murim Alliance is being formed at Mount Song; Taekyung believes Dark Heaven planned the Gate incident, while Jin Wikyung's Hubei arrangement was designed to create an opening among rival unorthodox factions.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Taekyung's party is traveling by two swift ships along the Yangtze toward Henan, and Taekyung's training has nearly depleted his internal energy.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan.",
    "A large shark-like creature is approaching Taekyung in the Yangtze."
  ],
  "continuity_sources": [
    510,
    509
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "Will Taekyung complete the ten-day training, and what is the shark-like creature approaching him?"
  ],
  "safe_through": 510,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain established renderings including Energy-Dispersing Poison, Seven-Step Soul-Chasing Powder, Blood Fish, Mutated Minnow, innate qi, true-origin qi, Heart Demon, Returned to Youth, Demon-Sealing Formation, and New Murim Alliance; use oar, throwing blade, stern, fire qi, river bandit, and Stronghold Lord for this chapter's terms.",
    "Render 궁예 as Gung Ye with an explanatory footnote, and render 연계 퀘스트 as Linked Quest and 가짜 무림인-2단계 as Fake Murim Martial Artist—Stage 2."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 510
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

## Korean source

```text
＃511화



사방이 어둠에 잠긴 깊은 밤. 돛을 활짝 펴고 쾌속하게 나아가는 두 척의 선박이 있었다.

촤아아악.

밤눈이 밝은 뱃사람이라면 선박의 범상치 않은 속도에 한 번, 그리고 선박의 희미한 횃불 너머로 보이는 깃발에 두 번 놀랄 수밖에 없었다.

장강수로맹(長江水路盟).

푸른 염료로 적힌 이 다섯 글자야말로, 이토록 드넓은 장강을 안전하고 자유롭게 오갈 수 있는 확실한 통행증이라고 할 수 있었다.

하지만 그것은 통행증인 동시에 약탈자의 상징이기도 했다.

“저건…….”

“자, 장강수로맹! 수적 놈들이다!”

“꺄악!”

놀잇배를 띄워 놓고 잔치를 벌이던 풍류객들은 난리가 났지만, 조금 떨어진 곳에서 그물을 걷던 어부들의 반응은 달랐다.

“지랄헌다. 술이나 마저 퍼먹을 것이지 비명은 왜 질러?”

“신경 쓰지 말게. 하루 이틀 일도 아니고. 그런데 저게 장강수로맹이 자랑하는 바로 그 쾌조선인가?”

“쾌조선이라면 전에 한 번 본 적이 있지. 겁나게 빠른 걸 보니까 확실혀.”

“나도 저런 배 한 척만 있으면 소원이 없겠군.”

“고기를 얼마나 더 잡으려고?”

“뭔 소린가. 쾌조선이 있는데 무슨 부귀영화를 누리자고 고기를 잡아? 바로 수적으로 갈아타야지.”

본래 어부와 수적은 한 끗 차이다. 생계가 어려워지면 엊그제까지 물고기를 잡던 그물과 작살을 들고 약탈자로 변모하는 것이다.

그래서인지 그들은 수적을 딱히 두려워하는 기색이 없었다.

“오, 이쪽으로 오는디?”

“놔두게. 그래 봤자 우리는 안 털어 갈 테니.”

“염병, 가진 게 없으니까 수적 놈들도 안 털어 가네.”

어부들은 대화를 나누며 흥미진진하게 상황을 구경했다.

어부 역시 거칠기로는 둘째가라면 서러운 뱃사람들. 세상 물정 모르는 얼뜨기 수적도 어부는 안 건드렸다.

겨우 푼돈을 뜯으러 왔다가 작살에 꿰이는 수가 있으니까.

그건 장강수로맹 입장에서도 크게 다르지 않았다. 몇 푼 얻기 위해 어부들을 약탈하는 건 수지타산에 어긋나는 것이다.

그러니 어부들 입장에서는 남의 집 불구경하는 심정이었다.

하지만 잠시 후, 더욱 속도를 높여 사라지는 쾌조선을 본 그들은 고개를 갸우뚱거렸다.

“어, 그냥 가네?”

“그러게 말일세. 저 놀잇배에 건드리면 재미없을 만큼 대단한 집안 자제라도 있나?”

“그런 것치고는 신분도 확인 안 하고 휙 가 버리던디.”

“됐네. 무슨 상관인가. 더 늦어지기 전에 그물이나 마저 걷고 돌아가자고.”

“어, 그려.”

두 척의 쾌조선이 아무 일 없이 사라지자 놀잇배에서는 다시 흥겨운 음악 소리가 흘러나왔고, 입맛을 다신 어부들은 신경을 끈 채 자신들이 할 일에 열중했다.

고작 반 시진 뒤, 어디선가 정체 모를 괴성이 들려오기 전까지는 그랬다.

“끼얏메우!”

맨 처음, 그 괴성을 들은 어부들은 대수롭지 않게 생각했다.

“거 참. 적당히 해야지. 시끄럽게들 노네.”

“놀 줄 아는 놈인가 보군.”

“가뜩이나 힘들어 뒤지겄는디 끼얏메우 같은 소리 허네. 확 그냥 배 밑창에 구멍을 뚫어 버릴라.”

신경질적으로 중얼거린 반백의 어부가 재차 그물을 잡아당기던 그때였다.

“간다! 간다! 간다! 숑 간다아악!”

“응. 그려, 내가 지금 간다. 이 개자석들아.”

작살을 집어든 어부가 눈깔을 뒤집으며 분노했다.

“시벌 안 되겄네. 내가 얼른 가서 밑창에 구멍 뚫고 올라니까, 아무도 말리지 마소.”

“잠깐, 잠깐만 기다려 보게.”

이제야 뭔가 이상함을 알아챈 어부들이 귀를 쫑긋 세웠다.

“이거…… 놀잇배에서 나는 소리가 아닌 것 같은데?”

“진짜네. 뭐여, 그럼.”

“그러니까 소리가 들려온 방향이 아마…….”

약속이라도 한 것처럼 동시에 고개를 불쑥 쳐든 어부들이 소리를 찾아 사방을 둘러보았다.

연주가 뚝 끊긴 놀잇배에서도 이게 뭔가 싶었는지, 휘황찬란한 비단옷을 걸친 남녀가 뱃머리에서 캄캄한 장강을 바라보고 있었다.

“잘못 들었나?”

“분명 이상한 소리를 들었는디.”

“허, 무슨 귀신에 홀린 것도 아니고.”

사람들이 반신반의하던 바로 그 순간.

콰아아아아!

거칠게 물살을 가르는 소리와 함께 한 사람이 모습을 드러냈다. 아니, 엄밀히 말하면 그는 혼자가 아니었다.

“……오메.”

“저, 저게 뭐여.”

마침내 불청객의 정체를 확인한 모두가 눈을 부릅떴다.

이 깊은 밤에 웬 청년이 상반신을 홀딱 벗은 채 장강을 가로지르는 것도 놀라운 일이었지만, 알 수 없는 줄에 묶여 앞에서 헤엄치는 거대한 생물체의 정체를 깨닫자 눈을 의심할 수밖에 없었다.

“사, 사어(鯊魚)! 사어다! 사람이 사어를 타고 있다!”

누군가의 입에서 터져 나온 외침이 순간 내려앉았던 적막을 깨트렸다.

그리고 모두가 깨달았다. 저 미친 소리가, 자신들이 보고 있는 현실이라는 것을.

콰콰콰콰콰!

사어. 거대한 몸뚱어리에 생김새가 흉측하며, 타고난 성정이 잔혹해 사람마저 잡아먹는다는 괴이한 물고기.

바로 그 사어가 사람을 태운 채 헤엄치고 있었다.

심지어…….

“하, 한 마리가 아니다!”

“지느러미가 하나, 둘…… 다섯 개. 사어가 무려 다섯 마리!”

실로 경악할 노릇이었다. 주로 대해(大海)에서 서식하는 사어가 장강에 나타난 것도 흔치 않은 일이지만, 무려 다섯 마리가 한곳에 모여 있다니.

하지만 고작 그 정도였다면 어부들이 지금처럼 넋 놓을 일은 없었을 것이다.

그들이 할 말을 잃은 이유는 간단했다.

“……이보게, 내가 지금 꿈을 꾸고 있는 건가?”

“……나도 같은 꿈을 꾸고 있는 것 같은디.”

“내 눈에는 저 청년이 사어에, 그러니까. 어. 일종의 고삐를 씌워 몰고 있는 것 같은데,”

“몰러, 저게 뭐여. 무서워…….”

어부들의 대화처럼 다섯 마리의 사어에는 일종의 고삐가 물려 있었다.

다섯 개의 주둥이를 칭칭 휘감은 것은 은은한 빛이 감도는 밧줄로, 청년의 손에 꽉 붙잡혀 있는 상태였다.

“좌로 꺾어!”

청년이 외침과 함께 손목을 당기면.

콰아아아아!

사어들이 동시에 좌측으로 이동하고.

“우로 꺾어!”

다시 손목을 반대편으로 돌리면.

콰아아아!

그에 따라 사어들의 방향도 틀어진다.

쉽게 지치지 않는 체력과 빠른 속도를 지닌 다섯 마리의 사어가 정면에서 물살을 가르고, 청년은 두 발로 강물을 지탱하며 따라갔다.

앞서 지나간 쾌조선에 비해 빠르면 빨랐지, 결코 부족하지 않은 속도.

“……시방 저게 뭐시여.”

누군가가 넋 나간 목소리로 중얼거린 그 순간. 눈 깜짝할 새에 코앞까지 치달은 청년이 어부들을 향해 손을 흔들었다.

“어부 어서 오고.”

“……!”

“초면에 죄송한데, 길 좀 물을게요. 혹시 아까 배 두 척 안 지나갔어요? 아마 반 시진에서 한 시진 전이었을 것 같은데.”

놀잇배 습격을 계획하던 어부가 작살을 내리며 엉거주춤 대답했다.

“봐, 봤는디요. 쾌조선 말하는 거 아뇨?”

“맞는데요. 장강수로맹. 후미에 딱 봐도 성격 개같이 생긴 어린애 하나 서 있고.”

“그, 그건 모르겠고. 쾌조선이라면 저기 저짝으로 갔소. 한 반 시진쯤 전에.”

“반 시진이요? 거의 다 따라잡았네. 후우, 시벌 거. 피똥 쌌다.”

“……?”

뱃사람 못지않은 찰지고 걸쭉한 단어 선택에 어부가 멈칫한 그때, 청년이 손에 묶인 기이한 밧줄을 슬쩍 풀었다.

뒤늦게 사어 한 마리가 풀려난 것을 알아챈 어부들이 기겁했다.

“으헉!”

“사, 사어가 풀려났다!”

“뒤로! 뒤로! 노 저어!”

하지만 어부들이 우려하는 그런 상황은 벌어지지 않았다.

사어는 붕어처럼 온순하게 눈을 깜빡이며 청년을 바라볼 뿐이었고, 청년 역시 대수롭지 않은 표정으로 입을 열었다.

“사어? 아, 상어 말씀하시는 거구나.”

“지, 지금 이게 뭐 하는 짓이오!”

“뭘 걱정하시는지는 아는데, 우리 애는 안 물어요.”

“우리 애?”

“시범 보여 드릴게요, 자. 지느러미.”

어부들의 눈이 툭 튀어나왔다.

청년이 손을 내밀기 무섭게, 눈을 뒤룩뒤룩 굴리고 있던 사어가 제 지느러미를 들이미는 것이 아닌가.

“보세요. 말 잘 듣죠? 착하다니까요.”

착한 게 아니라, 착해진 것 같은데.

어부들은 목구멍까지 차오른 말을 꿀꺽 삼켰다.

너덜거리는 사어의 지느러미와 벌벌 떨리는 몸체는, 그냥 기분 탓이다. 기분 탓이어야 한다.

청년은 어부들이 자신의 근육을 바라보는 걸 아는지 모르는지, 태연하게 말을 이어 갔다.

“애가 원래 분노 조절 장애가 있는데, 저한테 처맞은 뒤로는 조절 잘하니까 괜찮을 겁니다. 이런 기회 또 없을 테니까 저한테 한 마리 분양받으세요.”

“예, 예?”

“답례요, 알려 주신 답례. 어차피 이제 슬슬 놔줘야 해서. 대신 먹을 것 좀 있습니까? 삼시 세끼 회만 먹었더니 배 속이 어항이 된 느낌이라.”

도대체 무슨 상황인지는 몰라도, 뭘 해야 신상에 이로울지는 본능적으로 안다.

어부는 사시나무처럼 떨며 품에 넣어두었던 요깃거리를 건네주었다.

“여, 여, 여기 있소.”

“아, 예. 가, 가, 감사합니다.”

밍밍하게 간을 맞춘 주먹밥을 받아 든 청년이 장난스럽게 씩 웃었다.

“그럼 많이 잡으세요.”

콰과과과과!

그것이 마지막이었다.

순식간에 저 멀리 어둠 속으로 사라지는 일인사어(一人四魚)의 모습을 멍하니 바라보던 어부들은, 그가 남기고 간 유일한 흔적을 바라보았다.

흠칫!

괜히 사람 하나 잘 못 건드렸다가 호되게 처맞고 이제는 사람 자체를 두려워하게 된 사어. 아니, 흰철갑상어는 몸을 부르르 떨었다.

그리고 새로운 주인이 된 어부는, 지금 이 순간 자신의 운명이 크게 바뀌었음을 깨달았다.

“……이거면 쾌조선 없어도 되겠네.”

수적계의 새로운 신성이 탄생하는 순간이었다.



* * *



장담하건대, 현대와 무림을 통틀어 나처럼 자연친화적인 수상스키를 경험해 본 사람은 없을 거다.

촤아아악!

“4번 상어. 자세가 흔들린다.”

흠칫!

“그래, 방금 움찔한 놈. 너. 개인주의냐?”

스스슥!

“그래, 지금처럼만 해라. 너 혼자 가는 거 아냐. 친구들이랑 지느러미 맞춰서 함께 가는 거야.”

물론 폭력을 좀 쓰긴 했다.

주먹 몇 대 맞는 것으로는 성에 안 찼는지 계속 덤벼들기에 지느러미도 좀 다져 주고, 이빨도 몇 개 뽑았다.

환경 단체가 봤다면 천인공노할 자연 파괴범이요, 죽어서도 고통받을 어류 학대범이겠지만 처음부터 신경 안 썼다.

‘내가 뭐 샹크스도 아니고.’

덤벼드는 상어가 배고파 보인다고 팔 한 짝 내주는 대인배는 고전 만화책에서만 등장하는 거다.

나는 한 놈을 붙잡아 정신 교육한 뒤 동족을 불러왔고, 상어 수상스키단을 창단했다. 일명 잡으리 양식.

‘그래도 이 녀석들 없었으면 여기까지 못 왔지.’

나는 흐뭇한 눈빛으로 훌륭하게 임무를 수행해 준 수상스키 단원들을 바라보았다.

한나절 간 휴식과 이동을 반복하며 한때 바닥을 쳤던 공력도 어느 정도 보충했고, 쾌조선과의 거리도 상당히 좁혔다. 열심히 일한 노동의 대가는 자유다.

“자, 다들 가라.”

녀석들의 주둥이에 묶은 밧줄, 아니 지난번에 꿍쳐 두었던 [수신룡의 힘줄]을 풀어준 그때였다.

“……이런 미친놈을 봤나.”

나는 불쑥 귓가를 파고드는 목소리에 고개를 돌렸다.

깊은 어둠 너머, 수면을 밟으며 걸어 나오는 한 사람이 있었다.
```

## Final English reading copy

```markdown
# Chapter 511

It was the dead of night, with darkness enveloping everything around them. Two vessels sailed swiftly forward with their sails spread wide.

*Sssshhh!*

Any sailor with good night vision would have been startled once by the vessels’ extraordinary speed, then twice by the flag visible beyond their faint torchlight.

The Yangtze River Channel League.

Those five characters, written in blue dye, served as a guaranteed pass allowing one to travel freely and safely across the vast Yangtze.

But the flag was both a pass and a symbol of raiders.

“What the…”

“L-look! The Yangtze River Channel League! They’re river bandits!”

“Eek!”

The pleasure boat’s passengers, who had been holding a feast on the water, fell into a panic. The fishermen hauling in their nets some distance away, however, reacted differently.

“What the hell are they screaming about? They ought to finish guzzling their booze.”

“Don’t worry about it. It’s not like this is the first time. But is that the swift ship the Yangtze River Channel League is so proud of?”

“I’ve seen one of those once before. It sure is damn fast, so it probably is.”

“If I had just one ship like that, I wouldn’t want for anything.”

“How many more fish are you planning to catch?”

“What are you talking about? If I had a swift ship, why would I bother catching fish to chase wealth and glory? I’d switch over to being a river bandit right away.”

There was only a hair’s breadth between a fisherman and a river bandit. When making a living became difficult, a person could take the net and harpoon they had used to catch fish until the day before and transform into a raider.

Perhaps that was why the fishermen did not seem particularly afraid of river bandits.

“Oh, they’re coming this way.”

“Leave them be. It’s not as though they’ll rob us anyway.”

“Damn. We don’t own enough for even river bandits to bother robbing us.”

The fishermen chatted as they watched the situation with keen interest.

Fishermen were sailors second to none when it came to toughness. Even foolish river bandits who knew nothing about the ways of the world avoided messing with them.

They might come looking to extort a few pennies, only to end up skewered on a harpoon.

The Yangtze River Channel League was no different. Robbing fishermen for a few coins simply was not worth the trouble.

So from the fishermen’s perspective, this was like watching another man’s house burn down.

But a little while later, they watched the swift ships pick up speed and disappear into the distance. The fishermen tilted their heads.

“Huh? They’re just leaving?”

“So they are. Do you think some important young master from a powerful family is aboard that pleasure boat—important enough that it wouldn’t be worth messing with them?”

“They didn’t even check anyone’s identity before speeding off.”

“Forget it. What does it matter? Let’s finish hauling in the nets and get home before it gets any later.”

“Yeah, all right.”

Once the two swift ships disappeared without incident, lively music began flowing from the pleasure boat again. The fishermen smacked their lips regretfully, then returned their attention to their own work.

That was how things remained until, just half a shichen later, an unidentified, monstrous cry rang out from somewhere.

“Kkyat-meu!”

At first, the fishermen who heard it did not think much of it.

“Good grief. They ought to show some restraint. They’re making an awful racket over there.”

“Looks like someone knows how to party.”

“I’m already half dead from exhaustion, and now they’re making noises like ‘Kkyat-meu.’ I ought to go punch a hole in the bottom of that boat.”

The half-gray-haired fisherman who had muttered irritably reached for his net again.

That was when another cry rang out.

“I’m going! I’m going! I’m going! I’m going zoom!”

“Yeah, yeah, I’m coming right now, you bastards.”

The fisherman snatched up a harpoon, his eyes rolling back in fury.

“Fuck this. I’ll hurry over, punch a hole in their hull, and come right back, so nobody try to stop me.”

“Wait. Just wait a moment.”

The fishermen finally realized that something was strange and pricked up their ears.

“This… doesn’t sound like it’s coming from the pleasure boat.”

“You’re right. Then what is it?”

“So the sound came from…”

As though they had made a pact, the fishermen all abruptly raised their heads and searched in every direction for the source of the noise.

The music stopped abruptly aboard the pleasure boat as well. Apparently wondering what was going on, men and women dressed in dazzling silk stood at the bow and stared out at the pitch-black Yangtze.

“Did we hear wrong?”

“I definitely heard something strange.”

“Good grief. It’s not as though we’ve been bewitched by a ghost.”

Just as everyone was beginning to doubt their own ears—

*Whoooosh!*

Along with the roar of water being violently split apart, a person appeared.

No, strictly speaking, he was not alone.

“……Oh, my.”

“W-what the hell is that?”

At last, everyone saw the identity of the uninvited guest and opened their eyes wide.

It was astonishing enough that a young man was crossing the Yangtze in the middle of the night with his upper body completely bare. But when they realized what the enormous creature swimming ahead of him was, bound by some unknown rope, they could hardly believe their eyes.

“A s-sa-eo! It’s a sa-eo! Someone’s riding a sa-eo!”[^1]

The shout that burst from someone’s mouth shattered the silence that had settled over the river.

And everyone realized that the bizarre noise they had heard was part of the reality unfolding before their eyes.

*Whoosh, whoosh, whoosh!*

A sa-eo—a monstrous fish with an enormous, hideous body and a naturally vicious temperament, said to devour even human beings.

That very fish was swimming with a person riding behind it.

And what was more—

“T-there’s more than one!”

“One fin, two… five! There are five sa-eo!”

It was truly horrifying. It was unusual enough for sa-eo, which mainly lived in the open sea, to appear in the Yangtze. But five of them had gathered in one place.

If that had been all, the fishermen would not have stood there so dumbfounded.

The reason they had been rendered speechless was simple.

“……Tell me, am I dreaming right now?”

“……I think I’m having the same dream.”

“It looks to me like that young man has put some sort of bridle on the sa-eo and is, well… driving it.”

“I don’t know what that thing is. It’s terrifying…”

Just as the fishermen had said, the five sa-eo had something resembling bridles in their mouths.

A faintly glowing rope had been wrapped tightly around all five snouts, and the young man gripped its other end firmly in his hand.

“Turn left!”

When the young man pulled his wrist along with the shout—

*Whoooosh!*

The sa-eo all moved to the left at once.

“Turn right!”

When he twisted his wrist in the opposite direction—

*Whoosh!*

The sa-eo changed course accordingly.

The five sa-eo had great stamina and tremendous speed. They split the water ahead of them while the young man followed behind, supporting himself on the river with both feet.

They were as fast as the swift ships that had passed earlier—if anything, faster.

“What in the world is that?”

Just as someone muttered in a dazed voice, the young man came rushing right up to the fishermen in the blink of an eye and waved at them.

“Welcome, fishermen.”

“……!”

“Sorry to bother you when we’ve just met, but I’d like to ask for directions. Did two ships pass through here earlier? It would’ve been somewhere between half a shichen and one shichen ago.”

The fisherman who had been planning to attack the pleasure boat lowered his harpoon and answered awkwardly.

“W-we saw ’em. You mean the swift ships, right?”

“That’s right. The Yangtze River Channel League. There was a kid standing at the stern who looked like a nasty little shit.”

“I-I don’t know about that. But if you mean the swift ships, they went over that way. About half a shichen ago.”

“Half a shichen? I’ve almost caught up. Whew, fuck me. I busted my ass getting here.”

“……?”

The fisherman hesitated at the young man’s rich, vivid choice of words, no less colorful than any sailor’s. Just then, the young man casually loosened the strange rope wrapped around his hand.

The fishermen belatedly realized that one of the sa-eo had been released and panicked.

“Urgh!”

“T-the sa-eo’s been released!”

“Back! Back! Row!”

But the situation they feared did not occur.

The sa-eo merely blinked at the young man as docilely as a crucian carp, while the young man opened his mouth with an unconcerned expression.

“Sa-eo? Oh, you mean a shark.”

“What the hell do you think you’re doing?”

“I know what you’re worried about, but my boy doesn’t bite.”

“Your boy?”

“I’ll show you. Here, fin.”

The fishermen’s eyes bulged.

The moment the young man extended his hand, the sa-eo, which had been rolling its eyes around, thrust out its fin.

“See? He listens well, right? I keep telling you, he’s a good boy.”

Not good. More like he had been made good.

The fishermen swallowed the words that had risen to their throats.

The ragged fin and trembling body of the sa-eo were just their imagination. They had to be.

Whether or not he knew that the fishermen were staring at his muscles, the young man continued speaking calmly.

“My boy has anger-management issues, but he’s been controlling himself well ever since I beat the shit out of him. You’ll be fine. You won’t get another chance like this, so why don’t you take one off my hands?”

“Pardon?”

“As thanks. For telling me where the ships went. I have to let them go soon anyway. But do you have anything to eat? I’ve had nothing but sashimi for three meals straight, and it feels like my stomach has turned into an aquarium.”

The fisherman had no idea what was happening, but he instinctively understood what would be best for his own safety.

Trembling like a leaf, he handed over the food he had tucked inside his clothes.

“H-h-here.”

“Ah, yes. Th-thank you.”

The young man accepted the blandly seasoned rice ball and flashed a playful grin.

“Then catch lots of fish.”

*Whoosh, whoosh, whoosh!*

That was the last they saw of him.

The fishermen stared blankly as the sight of one man and four fish vanished into the distant darkness in an instant. Then they looked at the only trace he had left behind.

*Shudder!*

The sa-eo had foolishly picked a fight with the wrong person, been thoroughly beaten, and now feared human beings themselves. The shark—or rather, the white sturgeon—trembled violently.

And the fisherman who had become its new owner realized that his fate had just changed dramatically.

“……I guess I don’t need a swift ship anymore.”

That was the moment a new Morning Star was born in the world of river bandits.

* * *

I can guarantee that no one in either the modern world or Murim has ever experienced water skiing as eco-friendly as mine.

*Sssshhh!*

“Shark number four. Your posture is wavering.”

*Flinch!*

“Yes, you who just flinched. You. Are you an individualist?”

*Swish!*

“Just keep going like that. You’re not going alone. Match fins with your friends and go together.”

Of course, I had used a little violence.

Apparently a few punches hadn’t been enough, because they kept charging at me. So I worked their fins over a little and pulled out a few teeth.

If an environmental group had seen me, they would have called me a nature-destroying criminal who outraged heaven and humanity, as well as an animal abuser who would suffer even in death.

But I hadn’t cared from the beginning.

*It’s not like I’m Shanks or anything.*

The kindhearted hero who offers up one arm because a shark looks hungry only exists in old comic books.

I grabbed one of them, taught it a lesson, called over more of its kind, and founded the Shark Water-Ski Team.

I called it the Catch-’Em Fish Farm.

*Still, I wouldn’t have made it this far without these guys.*

I looked fondly at the water-ski team members who had carried out their mission admirably.

By alternating between resting and moving for half a day, I had replenished some of the internal energy that had once bottomed out. I had also narrowed the distance to the swift ships considerably.

The reward for hard work was freedom.

“All right, everyone. Off you go.”

That was when I untied the ropes around their snouts—or rather, the Water God Dragon’s sinew I had stashed away last time.

“……You really are a lunatic.”

I turned my head at the voice that suddenly slipped into my ear.

Beyond the deep darkness, a person was walking toward me across the surface of the water.

[^1]: *Sa-eo* (鯊魚) and *sang-eo* are both Korean terms for “shark.” *Sa-eo* is the Sino-Korean reading, while *sang-eo* is the ordinary word.
```
