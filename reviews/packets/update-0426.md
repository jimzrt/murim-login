<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0426.txt",
      "sha256": "099c6de9c8f23554cf00c14f524b10a3d21522b62e1f155e9df4b391f9638262",
      "bytes": 13454
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f9e7b49ef2a12d2220938dea520da3c5fe91b4cb71d9ede2a3c41edba14b49f0",
      "bytes": 1537
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b213a7c4406336c5137abdeac2190f57d40bfbb0898c49492d7607f0ede27c9d",
      "bytes": 140921
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e60bbf7b290f22aaa7a0fa4b9538aeb10f7567cdc7283588116fda03cc523cf6",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9f0c39cc79621124b542f227afc19e8e2332995b02c1d0ff36bf8acfc5a48d48",
      "bytes": 1349
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "da86c6d4cd6372d2826205359a923a77c2c132143c8f3d7d734ba9534d16b0ac",
      "bytes": 622
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "88d7a1cb505bd7ad16b98ed3422f55cc3635ec184955db8d5012cf1f99d715b0",
      "bytes": 893
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6215f7362654a41f862e4fe8d577a2990d3b2f8e87a0fa9a63e58673884f3060",
      "bytes": 130170
    }
  ],
  "estimated_tokens": 9499
}
-->

# Durable State Update — Chapter 426

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 426. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 426. Profile updates may replace only one
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
  "chapter": 426,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 426,
    "continuity_sources": [426],
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
    "Jin’s Middle Dantian is open, allowing him to perceive the center and grain of magic and sever spells.",
    "Hero’s Soul fully healed Jin, removed all status effects, and restored all attributes.",
    "The Skeleton Warlord revived through Hero’s Soul as a Lv.160 Skeleton King.",
    "The Skeleton King is Jin’s friend and ally after sacrificing itself to save him.",
    "The Arch Lich is impaled by Hero’s Soul, whose golden radiance is consuming its mana and body.",
    "The Gate was nearing completion and was strengthening the Arch Lich.",
    "Jin recovered White Flame and launched One Annihilation at the Arch Lich and the Gate.",
    "The result of One Annihilation and the fate of the Arch Lich and Gate are unresolved.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    425,
    424
  ],
  "open_questions": [
    "Did One Annihilation destroy the Arch Lich?",
    "Did One Annihilation stop or destroy the enormous Gate?",
    "What condition are the Skeleton King and Hero’s Soul in after the attack?",
    "What is Asmodeus’s current status and location?"
  ],
  "safe_through": 425,
  "temporary_decisions": [
    "Render 스켈레톤 킹 as Skeleton King and 골골이 as Bones.",
    "Render 영웅의 혼 as Hero’s Soul and 치유의 빛 as the light of healing.",
    "Preserve the Arch Lich’s archaic, contemptuous register and Jin’s profanity."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 425
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 422
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force, opened his Middle Dantian, and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, the Skeleton Warlord is his captive undead commander, and the Arch Lich regards him as a possible Adversary.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 422
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 424
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

## Korean source

```text
＃426화



화아아악!

창날로부터 뛰쳐나온 거대한 화룡을 마주한 그 순간, 아크 리치는 깨달았다.

‘늦었다.’

피할 수 없는 공격.

미처 토해 내지 못한 스펠(Spell)과 완성 직전이었던 마력이 곧장 들이닥친 화염에 흩어진다.

고통도 잊은 채 굳어 버린 아크 리치를 향해, 겁화로 타오르는 화룡이 아가리를 벌렸다.

콰우우우우!

용의 포효와도 같은 굉음과 함께, 푸른 화염이 사방을 휩쓸었다. 공간이 일그러트리고 모든 것을 증발시키는 끔찍한 열기.

아크 리치는 자신을 둘러싼 마력과 방어막이 녹아내리는 것을 느꼈다. 실로 오랫동안 잊고 있던 감각까지도.

‘뜨겁구나.’

화륵!

푸른 겁화가 아크 리치의 시야에 가득 찼다. 그의 전신을 휩쓸며 지나간 화룡은 멈추지 않고 뻗어 나갔다.

화룡이 향하는 곳은 폐허가 된 도시의 중심에 우뚝 선 거대한 검은 문.

바로 게이트(Gate)였다.

‘안 돼!’

아크 리치는 붉은 안광을 부릅뜨며 손을 뻗었지만, 음성은 흘러나오지 않았고 화룡은 제 몸만 한 게이트를 그대로 집어삼켰다.

수십만에 달하는 인간의 생명력을 바탕으로 모여진 미증유의 마력과 화염이 부딪친 그 순간, 눈부신 섬광이 터져 나왔다.

파아앗!

그것은 수백, 수천 킬로미터 밖에서도 보일 법한 빛의 기둥이었다.

어둠과 푸른 화염이 서로를 향해 충돌하며 이내 섞여든다. 힘겹게 버티고 있던 빌딩 숲이 허리를 굽혔고 둥근 바람의 고리가 터져나갔다.

쿠구구구궁-

감히 말로는 표현할 수 없는 굉음과 진동이 세상을 떨어 울렸다.

잿빛 하늘이 갈라지며 도시 전체를 자욱하게 감싸고 있던 잿빛 안개가 아지랑이처럼 흩어졌다.

그리고 이 모든 것들이 어느 날의 꿈이었던 것처럼, 고요한 정적이 찾아왔다.

‘아.’

아크 리치는 공허한 시선으로 세상을 바라보았다.

조금 전과 다를 것 없는 풍경이었으나, 그는 알 수 있었다. 자신을 포함한 모든 것이 달라졌다는 것을. 모래성처럼 무너져 내렸다는 것을.

아크 리치는 천천히 고개를 돌렸다. 파르르 떨리는 붉은 안광이 철탑처럼 우뚝 서 있는 한 사람에게 닿았다.

- 네놈을 죽였어야 했는데.

정적을 깨트리는 한마디.

핏기 하나 없는 안색을 한 진태경이 입을 열었다. 끊임없는 전투를 치르며 누적된 데미지와 정신적 피로로 금방이라도 쓰러질 것 같았지만, 목소리만큼은 여전히 힘을 잃지 않았다.

“그러게. 빨리 죽이지 그랬냐.”

아크 리치는 입을 다물었다. 분명 진태경의 숨통을 끊을 기회를 놓친 것은 그의 잘못이었다.

아주 잠깐의 방심이, 모든 것을 물거품으로 만들어 버린 것이다.

‘왕이시여. 부디 이 불충한 신하를 용서하소서.’

아크 리치는 어딘가에 있을 자신의 왕에게 용서를 빌었다.

만약 지체하지 않고 진태경을 죽였다면, 저 인간의 편에 선 몬스터가 새로운 존재로 거듭나 그의 가슴에 빌어먹을 검을 박아넣지 않았다면…… 모든 것은 계획대로 흘러갔을 터였다.

그는 살아남아 게이트를 완성시켰을 테고, 감히 헤아릴 수조차 없는 무수한 수의 몬스터 군단을 이끌며 버러지 같은 인간들을 잡아 죽이고 도시를 불태웠을 것이다.

언젠가 돌아올 위대한 왕을 기다리며.

하지만 완벽하다고 생각했던 계획은 보기 좋게 어그러졌다.

고작 한 명의 인간, 진태경의 등장으로 인하여.

점점 사그라들던 아크 리치의 붉은 안광이 마지막 힘을 다해 타올랐다.

스스로에게 하는 다짐이자, 복수에 대한 맹세가 진태경을 향해 흘러나왔다.

- 날 기억해라. 언젠가 너희의 영혼을 맨발로 짓밟을 이 몸을.

진태경이 가래를 탁 뱉었다.

“곧 뒈질 새끼가 헛소리는. 아스모데우스 개새끼 해 봐.”

스켈레톤 킹이 머뭇머뭇 입을 열었다.

- 아스모데우스 개새끼…….

“……너 말고.”

- 아, 안다. 그냥 한번 해 봤다. 그런데 너무나도 불경한 말을 한 것 같아 기분이 좋지는 않군.

“뭐가 어때서. 너도 이제 왕이잖아.”

- 어, 그러네.

죽음의 강에 맹세코, 저 두 놈을 찢어 죽이리라.

아크 리치는 진태경과 스켈레톤 킹을 향해 두 손을 뻗었다.

뼈로 이루어진 손이 저 멀리 떨어진 둘을 으스러트릴 것처럼 움켜쥐었지만, 아무런 일도 벌어지지 않았다.

그 대신 어디선가 불어온 바람이 그의 전신을 스쳤다.

솨아아아.

그건 붕괴였다. 아크 리치의 손이 재가 되어 흩어지는 것을 시작으로, 그를 이루는 모든 것들이 허물어지기 시작했다.

팔, 다리, 가슴, 그리고 마침내 붉은 안광이 자리한 두개골까지.

- 부디 살아남거라. 다시 만나게 될 그 날까지…….

원한에 찬 마지막 음성이 바람에 섞여 사라진다.

더욱 거세진 바람은 한때 아크 리치라 불렸던 잿가루를 품고 계속해서 나아갔다.

바람이 스칠 때마다 일섬의 범위에 휘말렸던 모든 것들이 가라앉고 무너졌다. 무너진 고층 빌딩, 콘크리트 더미, 뒤집힌 자동차와 이미 생명이 떠난 사체들……

그리고 더 큰 전쟁의 시작점이 되었을, 미처 완성되지 못한 거대한 게이트까지.

푸스스스슥.

말없이 그 광경을 바라보고 있던 진태경의 귓가에, 이 자리에서 오직 그만이 들을 수 있는 맑은 종소리가 울려 퍼졌다.

띠링. 띠링. 띠링.

눈 앞을 가리는 수많은 시스템 메시지들. 그것은 마침내 모든 것이 끝났음을 알리는 축포였다.

그러나 모든 힘을 다한 진태경의 몸뚱어리는 이미 지면을 향해 기울어지고 있었다.

‘해냈다.’

오직 한 가지 생각을 끝으로, 아주 편안하고 깊은 잠이 찾아왔다.

그리고 쓰러지는 진태경의 신형을 조심스럽게 받아 안은 스켈레톤 킹은 볼 수 있었다.

그의 입가에 번져 있는 잔잔한 미소를.

- ……고생했다.

간악하지만, 역시 썩 괜찮은 인간이란 말이지.

마음속으로 작게 중얼거린 스켈레톤 킹은, 진태경을 안전하고 편안한 자리로 옮기려다가 잊고 있던 한 가지를 떠올렸다.

- 아, 맞다. 그 검.

‘영웅의 혼’이라고 하던가? 누가 붙인 이름인지는 모르겠지만 신비한 힘이 깃들어 있는 건 확실했다.

스켈레톤 워로드였던 자신을 소멸 직전에 일깨운 것도, 저 무시무시한 아크 리치에게 심각한 타격을 입힐 수 있었던 것도 그 검 덕분이었다.

- 깜빡할 뻔했네. 그건 반드시 챙겨 놔야지.

스켈레톤 킹이 그것을 찾기까지는 그리 오랜 시간이 걸리지 않았다. 마지막까지 표적의 가슴에 박혀 있던 검은 조금 전까지만 하더라도 아크 리치가 서 있던 그 자리에 얌전히 놓여 있었으니까.

하지만 [영웅의 혼]을 집어 든 스켈레톤 킹은 고개를 갸웃거렸다.

- 어, 뭔가 이상한데.

그건 뭐라 설명하기 힘든, 묘한 느낌이었다.

딱 꼬집어 말할 수는 없었지만 뭐랄까. 명검인 것은 맞아도 예전 같은 신비로움이 느껴지지 않는다고 해야 하나.

- 내가 검을 잘못 찾은 건가?

하지만 스켈레톤 킹이 주위를 샅샅이 뒤지고, 검을 자세히 살펴봐도 달라지는 것은 없었다.

한동안 황금빛 두개골을 긁적이며 고심하던 스켈레톤 킹은 마침내 한 가지 결론을 내렸다.

- 으음. 맞겠지, 뭐.

어차피 한순간의 느낌일 뿐이라고 생각했다. 그가 기억하고 있는 검의 모양새도 같았고, 마지막 순간 아크 리치의 가슴에서 떨어지는 걸 직접 보기까지 했으니까.

‘그런데 왜 이렇게 찝찝하지?’

도무지 알다가도 모를 일이다. 고개를 내저은 스켈레톤 킹은 검을 자신의 골반뼈 사이로 찔러넣어 수납했다.

곧장 쓰러져 있는 진태경을 향해 걸음을 옮기는 그는 알지 못했다.

모든 힘을 소진한 진태경이 의식을 잃은 순간, 저 멀리 흩어지는 바람 사이로 안개와도 같은 검은 기운이 섞여 들어갔다는 것을.

그와 함께 [영웅의 혼]에 서려 있던 황금색 빛이 검은 기운을 쫓아 사라졌다는 것 역시도.

그러나 한 존재는 달랐다.

바람에 섞여 어딘가로 흘러간 검은 기운.

진태경에 의해 대부분의 힘을 잃고 아주 작고 힘없는 영혼의 한 조각으로 전락한 아크 리치는, 자신을 가로막은 눈부신 황금빛을 보며 눈을 부릅떴다.

‘이런 말도 안 되는.’

형체를 잃기 전, 아크 리치가 진태경과 스켈레톤 킹에게 했던 말은 한 치의 거짓도 없는 사실이었다.

그는 머지않은 미래에 반드시 돌아올 것이며, 이전보다 더욱 강대한 힘과 더욱 많은 몬스터 군단으로 이 땅을 피로 물들일 생각이었다.

라이프 포스 베슬(Life Force Vessel).

언데드만이 사용할 수 있는 최고위 흑마법이자 영혼의 조각을 보관할 수 있는 그것이 있다면 영원한 소멸은 피할 수 있다.

아니, 피할 수 있을 것이라 여겼다. 저 찬란한 황금색 빛이 자신을 가로막기 전까지는.

- 너는, 너는 무엇이냐!

지금의 아크 리치는 하찮은 영혼의 일부에 불과했고, 빛으로부터 전해지는 힘에 비할 바가 아니었다.

분노와 당황, 두려움으로 인해 검은 기운이 크게 일렁였다.

그러나 아크 리치의 사념(思念)이 전해졌음에도 황금색 빛은 어떤 반응도 보이지 않았다. 그저 더욱 밝게 빛나고, 크기를 부풀릴 뿐이었다.

그리고 다음 순간, 아크 리치는 빛의 정체를 깨달았다.

저것은 마법이 아닌 영혼이다. 한때 자신이 깨트리고 짓밟았던 누군가의 영혼. 이미 형체를 잃었음에도 오직 의지로 검에 깃들어 있던 영혼의 한 파편.

아크 리치는 불현듯, 뇌리 깊숙이 치워두었던 기억 중 하나를 떠올렸다.



‘고결하구나, 인간이여. 이름이 무엇이냐.’



피가 강을 이루고, 시체가 산을 이루었던 그 날. 파괴와 죽음만이 가득하던 도시에서 마지막까지 서 있던 한 인간.

- 레이페이.

아크 리치, 아니 검은 기운의 움직임이 우뚝 멈췄다.

허공에서 터져 나온 눈부신 황금빛이 파도처럼 그를 덮쳤다.

화아아악-!

‘……빌어먹을.’

그리고 그것이 아크 리치의 마지막 사념이었다.



* * *



본대가 결집 되어 있는 전장의 상황은 치열했다.

S급 헌터들이 결사대의 길을 열어 주기 위해 일부 병력과 함께 후방으로 이동한 사이, 수만의 몬스터 군단은 기회를 놓치지 않고 달려들었다.

「파이어 레인(Fire Rain)!」

콰과과과광!

후열에 위치한 마법사 부대가 광역 마법을 퍼붓자 불의 비가 쏟아져 내린다.

수백의 몬스터가 숯덩이가 되어 타 죽는 광경에 마법사들이 주먹을 불끈 움켜쥔 그때였다.

쐐애애액! 퍼걱!

「……어?」

마법사 중 하나가 어리둥절한 얼굴로 얼굴에 묻은 피를 닦았다.

조금 전까지만 하더라도 서로를 향해 웃고 있던 동료의 얼굴이 사라져 있었다. 아니, 터져 나갔다.

저 멀리서 빛살처럼 파고든 검은 창에 의해.

쐐애애애액, 펑!

다시 한번 날아든 창이 예닐곱 명의 마법사를 꼬치처럼 꿰뚫은 후에야 뒤늦은 비명이 울려 퍼졌다.

「으아아악!」

「데스나이트! 데스나이트다!」

「씨발, 그게 뭔 개소리야! 다 처리한 거 아니었어?」

「아, 아닌 것 같습니다! 저 중에서도 정예들을 따로 숨겨 둔 것 같습니다!」

누군가의 말은 곧 현실로 나타났다.

S급 헌터들의 부재를 확실히 알아차린 정예 몬스터들이 전장에 모습을 드러냈고, 막을 수 없는 살육이 시작되었다.

서거걱!

콰아아앙!

데스나이트, 리치, 보이지 않던 수십 마리의 와이번이 나타나 맹공을 퍼부었다.

사람들은 끝없이 죽어 나갔고, 몬스터는 끊임없이 밀려왔다.

S급 헌터들조차 자리를 비운 상황. 목숨을 걸고 버티던 사람들의 얼굴 위로 짙은 절망이 드리워졌다.

‘전부 끝이다.’

그리고, 모두가 죽음을 떠올린 바로 그 순간.

쉬이이익!

누군가의 몸을 베어 가던 데스나이트의 검이 우뚝 멈췄다.

아니, 잿가루가 되어 허물어졌다.

“이, 이게 뭐……?”

가까스로 목숨을 건진 헌터가 주위를 확인하고 입을 딱 벌렸다.

믿을 수 없는 광경이었다.

처음으론 수백이 쓰러지고, 그다음엔 수천이 허물어졌다.

이내 수만 마리에 달하는 몬스터들이 잿가루가 되어 스러지고 있었다.

솨아아아아.

바야흐로, 전쟁의 끝이었다.
```

## Final English reading copy

```markdown
# Chapter 426

*Fwoooooosh!*

The instant the Arch Lich faced the enormous fire dragon that burst from the spearhead, it realized the truth.

*Too late.*

An unavoidable attack.

The Spell it had not yet managed to unleash and the mana that had been on the verge of completion scattered beneath the flames rushing straight toward it.

The fire dragon, blazing with hellfire, opened its jaws at the Arch Lich, which had frozen in place, oblivious even to the pain.

*Kwooooooong!*

Along with a thunderous roar like that of a dragon, blue flames swept in every direction. A terrible heat distorted space and vaporized everything.

The Arch Lich felt the mana and barriers surrounding it melt away. It even felt a sensation it had truly forgotten for a very long time.

*It’s hot.*

*Fwoosh!*

Blue hellfire filled the Arch Lich’s vision. The fire dragon swept over its entire body and continued onward without stopping.

The fire dragon was headed toward the enormous black door standing tall in the center of the ruined city.

The Gate.

*No!*

The Arch Lich opened its red eye-lights wide and reached out, but no voice came from it, and the fire dragon swallowed the Gate—as large as itself—whole.

At the moment that the unprecedented mana gathered from the life force of hundreds of thousands of humans collided with the flames, a blinding flash erupted.

*Fwoosh!*

It was a pillar of light that could probably be seen from hundreds, even thousands, of kilometers away.

Darkness and blue flames collided with one another, then soon blended together. The forest of buildings that had been struggling to remain standing bent at the waist, and a ring of wind burst outward.

*Krrrrooooom—*

A thunderous roar and vibration beyond anything words could express shook the world.

The gray sky split apart, and the gray fog that had densely shrouded the entire city scattered like heat haze.

And then, as if all of it had been a dream from some distant day, a quiet stillness descended.

*Ah.*

The Arch Lich gazed at the world with hollow eyes.

The scenery looked no different from before, but it knew. Everything, including itself, had changed. Everything had collapsed like a sandcastle.

The Arch Lich slowly turned its head. Its trembling red eye-lights reached the person standing tall like an iron tower.

—“I should have killed you.”

The single sentence broke the silence.

Jin Taekyung opened his mouth, his complexion utterly bloodless. The accumulated damage and mental exhaustion from his endless battles made him look as though he might collapse at any moment, but his voice alone had not lost its strength.

“Yeah. You should’ve killed me sooner.”

The Arch Lich closed its mouth. It was certainly its own fault for missing the chance to cut off Jin Taekyung’s breath.

A momentary lapse in vigilance had turned everything to nothing.

*My king. Please forgive this disloyal servant.*

The Arch Lich begged forgiveness from its king, wherever he might be.

If it had killed Jin Taekyung without delay, if the monster that had taken the human’s side had not been reborn as a new being and driven that damned sword into its chest… everything would have proceeded according to plan.

It would have survived and completed the Gate. Leading an innumerable monster army beyond imagination, it would have hunted down and killed those verminous humans and burned the city to the ground.

While waiting for the great king to return someday.

But the plan it had believed to be perfect had been thoroughly ruined.

By the arrival of a single human.

Jin Taekyung.

The Arch Lich’s red eye-lights, which had been gradually fading, flared with their last remaining strength.

A vow to itself and an oath of vengeance spilled toward Jin Taekyung.

—“Remember me. Remember this body, which will one day trample your souls beneath its bare feet.”

Jin Taekyung spat out a wad of phlegm.

“Big talk from a bastard who’s about to croak. Try saying, ‘Asmodeus is a fucking son of a bitch.’”

The Skeleton King hesitantly opened its mouth.

—“Asmodeus is a fucking asshole…”

“Not you.”

—“Ah, I know. I just wanted to try it once. But I cannot say that I feel good after uttering something so blasphemous.”

“What’s the problem? You’re a king now, too.”

—“Oh. That’s true.”

*I swear on the River of Death, I will tear those two apart.*

The Arch Lich stretched both hands toward Jin Taekyung and the Skeleton King.

Its skeletal hands clenched as if they would crush the two figures standing far away, but nothing happened.

Instead, a wind that had blown in from somewhere brushed against its entire body.

*Whoooooosh.*

It was collapse.

Beginning with the Arch Lich’s hands turning to ash and scattering, everything that made up its body began to crumble.

Its arms, legs, and chest, and finally even the skull containing its red eye-lights.

—“Please survive. Until the day we meet again…”

Its final voice, filled with resentment, vanished into the wind.

The wind grew stronger, carrying the ash that had once been called the Arch Lich as it continued onward.

Whenever the wind passed, everything caught within the range of One Annihilation sank and crumbled. Collapsed high-rise buildings, heaps of concrete, overturned cars, and corpses from which life had already departed…

And even the enormous, unfinished Gate that would have become the starting point of an even greater war.

*Fssshhh.*

As Jin Taekyung stared silently at the scene, a clear chime rang in his ears—the sound that only he could hear in this place.

*Ding. Ding. Ding.*

Countless System messages obscured his vision. They were a celebratory salute announcing that everything had finally ended.

But Jin Taekyung’s body, which had exhausted every last bit of its strength, was already tilting toward the ground.

*I did it.*

With that as his only remaining thought, a deep, peaceful sleep came to him.

And as the Skeleton King carefully caught Jin Taekyung’s falling body, it saw the faint smile spreading across his lips.

—“…You worked hard.”

*He is a cunning human, but he really is a pretty decent one.*

The Skeleton King murmured inwardly. Then, as it began to move Jin Taekyung to a safe and comfortable place, it remembered something it had forgotten.

—“Ah, that’s right. The sword.”

*Was it called Hero’s Soul?* It did not know who had given it that name, but it was certain that a mysterious power dwelled within it.

It was thanks to that sword that it had awakened on the verge of Erasure when it had been the Skeleton Warlord, and that it had been able to inflict serious damage on that terrifying Arch Lich.

—“I almost forgot. I need to make sure to keep it safe.”

It did not take the Skeleton King long to find it. The sword that had remained buried in the target’s chest until the very end was lying quietly in the place where the Arch Lich had stood only moments ago.

But after picking up **Hero’s Soul**, the Skeleton King tilted its head.

—“Huh? Something feels strange.”

It was a peculiar feeling, difficult to explain.

It could not put its finger on it, but how should it say this? The sword was certainly a fine blade, yet it did not have the same sense of mystery as before.

—“Did I pick up the wrong sword?”

But no matter how thoroughly the Skeleton King searched its surroundings or examined the sword, nothing changed.

After scratching its golden skull and pondering for a while, the Skeleton King finally reached a conclusion.

—“Hmm. I guess this is it.”

It decided that it was nothing more than a momentary feeling. The sword looked the same as the one it remembered, and it had even seen it fall from the Arch Lich’s chest with its own eyes.

*But why does this feel so unsettling?*

It was something it could not understand at all. The Skeleton King shook its head, then slid the sword between its pelvic bones to store it.

As it immediately headed toward Jin Taekyung, who lay collapsed on the ground, it did not know that the moment Jin Taekyung lost consciousness after exhausting all his strength, mist-like black energy had mingled with the wind scattering in the distance.

Nor did it know that the golden light clinging to **Hero’s Soul** had vanished as it pursued the black energy.

But one being was different.

The black energy that had flowed somewhere within the wind.

The Arch Lich, which had lost most of its power because of Jin Taekyung and had been reduced to a tiny, powerless fragment of a soul, opened its eyes wide as it saw the dazzling golden light blocking its path.

*This is impossible.*

The words the Arch Lich had spoken to Jin Taekyung and the Skeleton King before losing its form had been entirely true.

It would return in the near future. It intended to stain this land with blood using even greater power than before and an even larger monster army.

Life Force Vessel.

The highest-level black magic usable only by the undead, and a vessel capable of storing a fragment of the soul.

If it had that, it could avoid eternal Erasure.

No—it had believed it could, until that brilliant golden light blocked its path.

—“You… What are you?”

The Arch Lich was now nothing more than a pitiful fragment of a soul, incomparable to the power transmitted by the light.

The black energy writhed violently with rage, confusion, and fear.

But even though the Arch Lich’s thoughts reached it, the golden light showed no reaction. It merely shone more brightly and swelled larger.

And in the next moment, the Arch Lich realized the identity of the light.

*That is not magic. It is a soul.*

Someone’s soul—the one it had once shattered and trampled beneath its feet. A fragment of a soul that had already lost its form, yet remained within the sword through nothing but its will.

Suddenly, the Arch Lich recalled one of the memories it had pushed deep into the back of its mind.



*“You are a noble one, human. What is your name?”*



That day, when blood had formed rivers and corpses had formed mountains. A single human who had remained standing until the very end in a city filled with nothing but destruction and death.

—“Lei Fei.”

The movement of the Arch Lich—or rather, the black energy—stopped abruptly.

The dazzling golden light that burst through the air swept over it like a wave.

*Fwoooooosh!*

*…Damn it.*

And that was the Arch Lich’s final thought.



* * *



The situation on the battlefield where the main forces had gathered was fierce.

While the S-rank Hunters moved toward the rear with some of the troops to open a path for the suicide squad, the monster army numbering in the tens of thousands did not miss the opportunity and charged forward.

「Fire Rain!」

*Kwaaang!*

When the mage units positioned in the rear unleashed an area-wide spell, a rain of fire poured down.

The mages clenched their fists at the sight of hundreds of monsters burning to death as charred lumps of coal.

That was when—

*Whoooooosh! Thwack!*

「…Huh?」

One of the mages wiped the blood from their face with a bewildered expression.

The face of a comrade who had been smiling back at them only moments ago had disappeared.

No, it had burst apart.

Pierced by a black spear that had cut through the distance like a beam of light.

*Whooooooosh! Boom!*

Only after another spear flew in and skewered six or seven mages like meat on a spit did belated screams ring out.

「Aaaaargh!」

「Death Knights! It’s Death Knights!」

「Fuck, what the hell are you talking about? Didn’t we take care of all of them?」

「I-I don’t think so! It looks like they hid their elites separately among the others!」

Someone’s words soon became reality.

The elite monsters, having clearly noticed the absence of the S-rank Hunters, revealed themselves on the battlefield, and an unstoppable slaughter began.

*Slash!*

*Kwaaang!*

Death Knights, Liches, and dozens of Wyverns that had remained unseen appeared and launched a fierce assault.

People died without end, and monsters continued to surge forward.

With even the S-rank Hunters away from their positions, deep despair spread across the faces of those staking their lives to hold the line.

*It’s all over.*

And at the exact moment everyone thought of death—

*Shiiiiing!*

The Death Knight’s sword, which had been cutting through someone’s body, suddenly stopped.

No.

It crumbled into ash.

“W-What the hell…?”

The Hunter who had barely survived checked his surroundings and gaped.

It was an unbelievable sight.

First, hundreds fell.

Then thousands crumbled.

Before long, monsters numbering in the tens of thousands were turning to ash and scattering.

*Whoooooosh.*

At long last, it was the end of the war.
```
