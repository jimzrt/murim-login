<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0754.txt",
      "sha256": "ebba69fd9e509ff0ffc4ad6e551f754702cb0e8ff05f0e80099f03159f614430",
      "bytes": 12837
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3fc30f64762a04f2466ecfd57d0219dd14bef8a2941e4b276e07a5450d0483bc",
      "bytes": 1162
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "76106d29c46c72d3fe28532b2cb28b5b247852bd7b8ea18939c1784ce765b9f9",
      "bytes": 218279
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8da44b2771313b0ec03d2650e833004c3a3779b48a6b28367b47459a69af1317",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1eafa7014124cafc6eefca36e1259569ee5a6e1ed0247e79ee534d13b87aa965",
      "bytes": 2091
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "715a7982b0dd1a7ca4feba2b245177832431c292b3f481c1f021d5af1d0b1943",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "b7f9ab66fad939ba2ce5bd489a0e2f9eb32bd57210f9dd10ec70c655f36a3aca",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c31483eef9871d4053fc6e6089d447714924c2ef95204a767b94526f83844713",
      "bytes": 232117
    }
  ],
  "estimated_tokens": 9319
}
-->

# Durable State Update — Chapter 754

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 754. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 754. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 754,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 754,
    "continuity_sources": [754],
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
    "Jin Taekyung can use the Turtle Breath Technique, learned from the Slaughter Saint, to erase his vital energy and conceal his presence.",
    "Jin Taekyung and Choi Minwoo used the Skeleton King and two S-rank Magic Gems as bait in a trap for Leviathan.",
    "Leviathan emerged near an uninhabited island in the Philippine Sea and attacked the bait boat.",
    "Jin Taekyung struck Leviathan's mouth with a blue-white flame spear and rescued the Skeleton King.",
    "Jin Taekyung is confronting Leviathan in midair after the boat was destroyed.",
    "The Skeleton King values the modern world and fears becoming Leviathan's food."
  ],
  "continuity_sources": [
    753
  ],
  "open_questions": [
    "What will be the result of Jin Taekyung's confrontation with Leviathan?",
    "Can Jin Taekyung protect the Skeleton King and survive Leviathan's counterattack?"
  ],
  "safe_through": 753,
  "temporary_decisions": [
    "Render 유골사태 as boneshed.",
    "Keep samgyeopsal and ssamjang untranslated, with pa-chae rendered as scallion salad.",
    "Render 귀식대법 as Turtle Breath Technique."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 지능               | **Intelligence**               |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 753
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 753
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, the creator of the beginner-accessible Smiling Mana Cultivation Method, and a practitioner of the Turtle Breath Technique learned from the Slaughter Saint.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 753
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 753
- **Aliases:** None
- **Role:** Leviathan is an ancient S-rank sea monster and ruler of the sea that emerged near an uninhabited island in the Philippine Sea, attacked the bait boat, and is now confronting Jin Taekyung after being struck in the mouth by his blue-white flame spear.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

## Korean source

```text
＃754화



콰아아아!

초고온의 열기가 공기를 태우고 수분을 증발시키며 나아간다.

마치 유성처럼 떨어져 내리는 한 줄기의 불꽃. 눈을 부릅뜬 레비아탄은 앞서 찾아온 고통조차 잊은 채 몸뚱어리를 비틀었다.

서걱!

뜨겁다. 미사일도 우습게 막아 내는 비늘을 단번에 가르고 들어간 창날은 단순히 스친 것만으로도 수십 킬로그램의 살점을 베어 냈다.

아니, 불살랐다.

치지지지직!

엄습하는 작열통(灼熱痛)에 레비아탄은 소리 없는 비명을 내질렀다.

처음 눈을 뜬 그 날부터 지금까지, 줄곧 바다의 재앙으로 군림한 이 신화 속 괴수에게 있어 불에 의한 통증은 여전히 낯선 것이었다.

지금 이 순간, 빛살처럼 쾌속한 속도로 자신을 공격해 오는 저 인간만큼이나.

쉬쉬쉬쉭!

언제, 어떻게 쏘아 보냈는지는 모른다.

다만 날카로운 파공성과 함께 다섯 줄기의 화염이 쏘아졌고, 레비아탄의 머릿속에는 붉은 경고등이 켜졌다.

‘위험!’

고통으로 굳어 있던 거대한 몸뚱어리가 황급히 뒤틀렸다.

아슬아슬하게 화염이 서린 창들을 피해 낸 레비아탄이 마력을 일으켰다.

구구궁!

사방을 짓누르는 강대한 힘.

비록 상처는 아물지 않았으나, 마력의 질과 양은 하루 전에 비할 바가 아니다.

마력을 한껏 머금은 채 솟구친 파도가 레비아탄의 의지에 응하여 바람 없이도 나아갔다.

감히 바다의 지배자에게 덤벼든 한 인간을 향해.

그리고 하찮은 인간의 거죽을 뒤집어쓴 채, 동족마저 공격하는 변절자를 향해.

콰아아아아!

반경 수백 미터를 뒤덮은 거대한 그림자. 희미한 빛조차 스며들지 않은 어두컴컴한 파도 속에서 마력이 회오리쳤다.

“젠장, 나 맛없다니까…….”

스켈레톤 킹이 아연히 중얼거린 그 순간.

“꺼져라.”

다물어진 잇새 사이로 흘러나온 나지막한 음성. 그와 동시에 인간은, 진태경은 화염에 휩싸인 주먹을 뻗었다.

퍼엉!

멸염신권(滅炎神拳).

허공을 격하고 터져 나온 청백색의 화염이 파도의 중심을 찢어발겼다.

힘없이 허물어지는 물보라 사이를 뚫고 쇄도하는 자그마한 인영(人影)에, 레비아탄은 분노 어린 괴성을 토해 냈다.

- 노오오옴!

촤아아악!

사방에서 솟구친 물줄기가 진태경의 전신을 향해 쏘아졌다.

하나하나가 항공모함을 꿰뚫고도 남을 위력. 한낱 인간이라면 말할 가치조차 없다.

상대가 정말 한낱 인간이라면.

쉬릭.

공기가 사라졌다. 바람이 갈라졌다.

앞서 레비아탄을 향해 쏘아 보낸 것들과는 확연히 다른, 은빛 창날의 끝에서 불꽃이 피어올랐다.

화륵, 서걱!

검은 바다 위로 그어진 푸른 선.

마치 용의 꼬리처럼 부드럽게 나아간 청백색의 불꽃이 송곳처럼 들이닥친 물줄기를 불살랐다.

다시 한번 허공을 밟으며 속도를 더한 진태경은 느려진 시간 속에서 호흡을 가다듬었다.

‘몸이…….’

평소와 다르다.

오늘따라 손발이 무거웠고, 속도도 예전만 못했으며, 공력의 소모도 예상했던 것 이상으로 훨씬 빨랐다.

‘빌어먹을 디버프.’

[망가진 신체]가 전투에 끼친 영향은 엄청났다.

처음부터 존재하지 않았다면 모를까, 지능을 제외한 모든 능력치가 대폭 하락하면서 커다란 공백이 생긴 신체가 머리에서 전달된 명령을 제대로 수행하지 못하고 있었다.

바로 지금처럼.

퍽!

둔탁한 타격음과 함께 흔들리는 신형. 그러나 진태경은 신음을 삼키며 뒤이어 날아든 공격을 피했다.

퍼퍼퍼펑!

시야를 뒤덮으며 쇄도해 오는, 수백여 개에 달하는 물의 구(球).

마법사들이 워터 볼(Water Ball)이라 이름 붙인 공격 마법과 닮았지만, 저것들에 담긴 위력은 워터 볼 따위에 비할 바가 아니라는 것쯤은 진태경이 누구보다 잘 알고 있었다.

이곳에서 자신이 물러서는 순간, 다시 한번 눈앞의 괴물을 놓칠 수도 있다는 사실도 함께.

후우웅.

투명하리만치 새하얀 창신(槍身)이 몸을 떨었다. 사그라질 듯하던 화염이 거칠게 솟아오르며 자신의 존재를 알린다.

한껏 뒤로 젖혀진 신병이기를, 진태경은 비스듬히 내리그었다.

화룡신창 이 초식.

천격(天格).

화아아악!

눈부신 섬광이 어느덧 근방을 뒤덮은 어둠을 밝힌다.

사방에 가득한 물의 구를 증발시키며 떨어져 내리는 겁화가 괴물의 거대한 눈동자를 불그스름하게 물들였다.

- 감히, 감히 인간 따위가……!

비명과도 같은 외침과 함께, 레비아탄은 모든 마력을 끌어올렸다.

그그그그긍.

바다가 요동치고 머리 위로 드리운 먹구름이 울음소리를 토해 낸다.

레비아탄의 몸뚱어리를 방패처럼 감싼 마력의 막(膜)과 창날이 맞닿은 그 순간. 검게 물든 하늘에서 눈부신 섬광이 번뜩였다.

감히 신화에 맞선 한 인간을 향해.

화악!

느려진 세상 속, 수십 줄기의 낙뢰(落雷)가 아득한 상공으로부터 내리꽂혔다.

나올 때는 수십이었으나 마지막에 이르러 하나로 뭉쳐진 그 파괴적인 자연의 힘은, 무언가에 이끌리듯 한 곳을 향해 빨려 들어갔다.

츠츠츠츠!

“끄아아아아악!”

순간 바다를 물들인 무수한 섬광과 끔찍한 고통에 찬 비명.

전력을 다한 마력으로 창날을 막아 내고 있던 레비아탄의 마음에 환희가 차올랐다.

‘역시!’

무려 수십억 볼트에 이르는 전압(電壓)이다.

상대가 제아무리 강한 인간이라 할지라도, 하나로 뭉쳐진 저 낙뢰의 기둥에 직격당하고도 멀쩡할 수는 없었…….

‘뭐지?’

레비아탄의 거대한 눈동자가 깜빡였다.

서서히 사그라지는 섬광 너머, 지금쯤 낙뢰에 직격당하여 살이 타오르고 뼈가 바스러졌어야 할 인간이 멀쩡한 모습으로 자신을 바라보고 있었다.

심지어는 이 와중에도 약간 부끄럽다는 표정으로 말까지 건넨다.

“그, 쟤가 원래 겁이 많아.”

- ……?

“야, 그만 좀 해라. 너 그걸로는 안 죽어.”

뭐?

레비아탄은 자신도 모르게 고개를 옆으로 기울였다. 진태경의 어깨너머, 듣는 것만으로도 끔찍한 비명을 내지르고 있는 한 존재가 괴물의 동공에 비쳤다.

“끄아아아아…….”

서서히 볼륨이 줄어드는 비명.

김이 모락모락 피어오르는 자신의 몸을 슬쩍 둘러본 스켈레톤 킹이 머쓱한 얼굴로 들고 있던 검을 내렸다.

“아, 맞네. 나 해골이지.”

“타이밍 좋았다. 피뢰침 전략 굿.”

“이건 그냥 도와주려고 뽑은…… 아니, 역시 내 전략을 정확히 파악했군. 제법이야.”

- ……!

도대체 뭐지 이 새끼들은?

모든 상황을 받아들이지 못한 레비아탄은 순간 정신이 혼미해졌다.

그리고 그 찰나의 방심은, 물 샐 틈 없이 견고하던 마력의 흐름을 헝클어트리기에 충분했다.

콰직!

전체에 비하면 아주 작은 균열.

그러나 그것은 진태경이 누구보다 간절히 원했던 틈이었고, 창날에 깃든 화염은 흔들리는 마력을 부수며 목표를 향해 내리꽂혔다.

푸푹!

창날의 끝에서 비늘이 산산이 부서진다. 살과 뼈가 타오르는 끔찍한 고통 속에서 레비아탄은 본능적으로 몸부림쳤다.

- 크아아아아아!

쿠궁. 콰아아아아!

미친 듯이 요동치는 거체.

하지만 진태경은 여기에서 만족하지 않았다. 괴물의 피부 곳곳에 난 작은 뿔들을 붙잡은 채, 손아귀에 단단히 틀어쥔 창에 힘을 더했다.

푸우우욱!

자그마치 2m에 달하는 창신이 레비아탄의 미간을 파고들었다.

거대한 머리 덕에 죽음은 피할 수 있었으나 지금껏 겪어 본 적도, 상상할 수도 없던 격통에 몸과 정신을 지배당한 신화 속 괴물은 괴성을 내질렀다.

- 노오오오옴!

스아아아아!

끔찍하리만치 강력한 피어(Fear)가 레비아탄을 중심으로 뻗어 나갔다.

깊은 수심에서 웅크리고 있던 해양 생물들이 눈깔을 까뒤집으며 떠올랐고, 곧 들이닥칠 위험을 예견하고 저 멀리 도망치던 무수히 많은 새가 추락했다.

지금 이 순간, 레비아탄은 그 어느 때보다 분노하고 있었다.

‘죽인다. 반드시!’

누구도 알아볼 수 없을 만큼, 갈기갈기 찢어 죽여야 한다.

자신에게 이런 고통을 안겨 준 저 인간 놈과 동족을 배신한 변절자에게 가장 처참한 죽음을 내려야 했다.

그러나 레비아탄을 지배하고 있는 고통과 분노라는 감정 속에서, 두려움이 불쑥 고개를 내밀었다.

‘하지만 어떻게?’

하루 전 자신에게 이토록 큰 상처를 입힌 것으로도 모자라, 이목마저 속여 가며 함정으로 끌어들인 놈들이다.

특히 저 인간, 감히 자신의 머리에 무기를 박아 넣은 저 작은 생물체는 도무지 이해할 수 없는 힘을 지니고 있었다.

‘강하다. 내가 지금껏 봐 왔던 어느 인간보다.’

대격변 당시만 해도 상상도 할 수 없던 일이었다.

레비아탄은 다섯 개의 대양을 누비며 수많은 목숨을 바다 깊숙이 수장시켰고, 가장 강하다고 평가받는 인간들조차 그를 사냥하는 데에는 번번이 실패했으니까.

아니, 사냥하는 쪽은 언제나 레비아탄이었다.

그는 지배자로 태어났고 포식자로 살았다.

이 드넓은 바다에서 그는 언제나 포식자였고, 인간은 한 입거리도 되지 않는 사냥감이었다.

아득한 생애를 반추해도, 레비아탄을 굴복시킨 것은 한 존재뿐이었다.

그가 충성을 맹세한 주인.

마왕 아스모데우스.

- ……!

순간, 고통과 분노에 물들어 있던 레비아탄의 눈동자가 크게 뜨였다.

‘설마, 이놈이?’

분명 들어 본 적이 있었다.

그토록 강대했던 자신의 주인에게 대적한 어느 인간에 대해서.

비록 단 한 번도 마주친 적은 없었지만, 그 인간은 무수히 많은 몬스터를 쓰러트리며 자신의 힘을 입증했었다. 마왕 아스모데우스라는 거대한 이름을 마지막으로.

‘그렇다면 정말 이 인간이…….’

틀림없다. 이토록 강한 인간이 둘일 리가 없다.

레비아탄은 오해는 두려움이 되어 부풀어 올랐다.

어느샌가 분노가 사라진 그 자리에는, 오직 한 가지 생각으로 가득 채워져 있었다.

‘도망쳐야 한다. 최대한 멀리. 이놈을 피해서!’

분노? 투쟁심(鬪爭心)?

그런 것 따위는 아무런 의미도 없다. 주인으로 섬겼던 마왕 아스모데우스를 쓰러트렸다면, 자신의 운명 역시 정해진 것이나 다름 없으니까.

- 그어어어어!

레비아탄은 크게 울부짖으며 몸을 털었다.

더 이상 고통이 아닌 생존을 위한 몸부림으로 변한 그것은 어느 때보다 격렬했으나, 거대한 몸뚱어리에 이미 둥지를 튼 누군가에게는 아무런 영향도 주지 못했다.

“닥쳐. 닥쳐. 안 닥쳐?”

빡! 빡! 빡!

피가 튀고 살이 뭉개졌다. 엄청난 악력에 단단하기 그지없는 비늘이 배추처럼 뽑혀 나갔고, 주먹 끝에 실린 화염은 살과 뼈를 으스러트렸다.

퍽, 콰직!

- 커헉. 컥.

연이어 들이닥치는 고통에 레비아탄은 까무러칠 것 같았다.

도무지 인간이라고는 상상할 수조차 없는 힘. 결국 그에게 남은 길은 한 곳밖에 없었다.

심해(深海).

레비아탄이 처음으로 눈을 뜬 그곳. 그리고 어떤 적도 침범할 수 없었던 바다 깊숙한 미지의 영역.

그곳에 다다르면, 이 끈질기고 무서운 인간도 떨어져 나가리라.

콰륵!

물보라가 솟구친다. 얕은 수심을 벗어나 넓은 바다로 나아간 레비아탄은 깊숙이 헤엄쳤다.

그리고 다음 순간, 웃고 있는 인간의 얼굴을 보며 자신의 짐작이 틀렸음을 깨달았다.

“이제야 좀 같이 싸우겠네.”

뭐?

한 줄기 의문이 뇌리를 스친 그때.

솨아아아악!

무저갱처럼 컴컴한 바닷물 깊숙한 곳에서, 무수히 많은 무언가가 하나로 뭉쳐 레비아탄의 앞을 가로막았다.

뼈.

그것은 뼈였다.
```

## Final English reading copy

```markdown
# Chapter 754

*Whoooooom!*

Ultra-high heat scorched the air and evaporated the moisture as it advanced.

A single streak of flame fell like a meteor. Leviathan’s eyes widened as it twisted its body, forgetting even the pain that had come before.

*Shhk!*

Hot.

The spearhead sliced clean through scales that could shrug off missiles. A mere graze sheared dozens of kilograms of flesh from Leviathan.

No.

It burned them away.

*Hissssss!*

Overcome by searing pain, Leviathan let out a silent scream.

From the day it first opened its eyes until now, the mythical monster that had reigned as the calamity of the sea had always found pain caused by fire unfamiliar.

Just like the human attacking it at a speed as swift as light.

*Shh-shh-shh-shhk!*

Leviathan did not know when or how the attack had been launched.

All it knew was that five streaks of flame shot forward with a sharp ripping sound, and a red warning light came on in its mind.

*Danger!*

The massive body that had frozen from pain twisted frantically.

After narrowly avoiding the flame-wreathed spears, Leviathan summoned its magical power.

*Ruuumble!*

A tremendous force pressed down from every direction.

Its wounds had not yet healed, but both the quality and quantity of its magical power far surpassed what they had been a day earlier.

A wave surged upward, filled to the brim with magical power, then advanced without any wind, responding to Leviathan’s will.

Toward the human who had dared to challenge the ruler of the sea.

And toward the traitor who attacked its own kind while wearing the skin of a worthless human.

*Whooooooosh!*

A massive shadow covered a radius of several hundred meters. Magical power churned within the pitch-black wave, where not even the faintest light could seep through.

“Damn it, I told you I don’t taste good…”

The Skeleton King muttered blankly.

At that very moment—

“Get lost.”

A low voice slipped through clenched teeth.

At the same time, the human—Jin Taekyung—thrust out a fist wreathed in flame.

*Boom!*

Flame-Extinguishing Divine Fist.

Blue-white flames erupted through the air and tore apart the center of the wave.

A small human figure shot through the collapsing spray. Leviathan let out an enraged roar.

—You bastard!

*Whoooooosh!*

Streams of water surged up from every direction and shot toward Jin Taekyung’s entire body.

Each one possessed enough power to pierce an aircraft carrier. Against an ordinary human, there was no point even discussing the result.

That was true if the opponent was really an ordinary human.

*Shhk.*

The air vanished. The wind split apart.

Flames bloomed at the end of a silver spearhead, distinctly different from the ones Jin had sent flying at Leviathan earlier.

*Fwoosh. Shhk!*

A blue line was drawn across the black sea.

Blue-white flames advanced smoothly like a dragon’s tail, burning away the streams of water that thrust toward Jin like spears.

Jin Taekyung stepped on empty air once more and accelerated. Within the slowed passage of time, he steadied his breathing.

*My body…*

It was different from usual.

His hands and feet felt heavy today, his speed was slower than before, and his internal energy was being consumed much faster than he had expected.

*That damn debuff.*

The effect of **Broken Body** on the battle was enormous.

It might have been different if he had never possessed those capabilities in the first place. But with every attribute except Intelligence drastically reduced, the resulting void left his body unable to properly carry out the commands from his mind.

Just like now.

*Thud!*

His body shook from a dull impact.

Jin swallowed his groan and evaded the attack that came immediately after.

*Boom! Boom! Boom!*

Hundreds of spheres of water came rushing toward him, covering his field of vision.

They resembled the attack spell mages called Water Ball, but Jin Taekyung knew better than anyone that the power contained within them was incomparable to any ordinary Water Ball.

He also knew that the moment he retreated here, he might lose sight of the monster in front of him once again.

*Whoooom.*

The nearly translucent white shaft of the spear trembled.

The flame that had seemed ready to die out surged violently, announcing its presence.

Jin Taekyung swung the divine weapon, drawn far back, down at an angle.

Fire Dragon Divine Spear, second form.

Heavenly Strike.

*Fwoooooosh!*

A dazzling flash illuminated the darkness that had already swallowed the surrounding area.

The hellfire falling through the air evaporated the countless spheres of water filling every direction, and the monster’s enormous eye was stained reddish.

—How dare you! How dare a mere human…!

Along with the scream, Leviathan drew up all of its magical power.

*Ruuuuumble.*

The sea heaved, and the dark clouds hanging overhead let out a groan.

At the moment the spearhead met the barrier of magical power wrapped around Leviathan like a shield, a dazzling flash spread across the blackened sky.

Toward the human who had dared to stand against a myth.

*Fwoosh!*

Within the slowed world, dozens of bolts of lightning plunged down from the distant sky.

They emerged as dozens, but by the time they reached their destination, they had merged into one. That destructive force of nature was sucked toward a single point as though drawn there by something.

*Crackle, crackle, crackle!*

“Gyaaaaaaaah!”

The sea was dyed with countless flashes, accompanied by a scream filled with horrific pain.

Leviathan had been using all its magical power to hold back the spearhead, and joy filled its mind.

*As expected!*

The voltage reached billions of volts.

No matter how strong the human was, he could not possibly remain unharmed after taking a direct hit from that pillar of lightning—

*What?*

Leviathan’s enormous eye blinked.

Beyond the slowly fading flash, the human who should have been standing there with his flesh burned and his bones shattered by the lightning was staring back at Leviathan completely unharmed.

He even spoke, his expression slightly embarrassed.

“Uh, he’s always been a scaredy-cat.”

—…?

“Hey, cut it out. You’re not going to die from that.”

What?

Leviathan tilted its head without realizing it.

Over Jin Taekyung’s shoulder, a being screaming horribly appeared in the monster’s pupil.

“Gyaaaaaaaah…”

The scream gradually grew quieter.

The Skeleton King glanced over his body, which was giving off wisps of smoke, then awkwardly lowered the sword he was holding.

“Ah, right. I am a skeleton.”

“That was some great timing. The lightning-rod strategy was good.”

“I only drew this to help you… No, as expected, you saw through my strategy perfectly. Not bad.”

—…!

What the hell were these bastards?

Unable to process the situation, Leviathan’s mind grew hazy for a moment.

That instant of distraction was enough to disrupt the flow of magical power that had been as solid as a wall with no gaps.

*Crack!*

A tiny fissure compared to the whole.

But it was exactly the opening Jin Taekyung had been desperately waiting for, and the flame dwelling in the spearhead smashed through the wavering magical power and plunged toward its target.

*Thrust!*

The spearhead shattered the scales. Amid the horrific pain of flesh and bone catching fire, Leviathan thrashed instinctively.

—GRAAAAAAAH!

*Rumble! Whoooooosh!*

The enormous body writhed madly.

But Jin Taekyung was not satisfied.

Grabbing the small horns scattered across the monster’s skin, he poured even more strength into the spear clutched tightly in his hand.

*Shhhhuuuk!*

The spear shaft, nearly two meters long, dug into the center of Leviathan’s brow.

Its enormous head saved it from death, but the mythical monster, dominated by pain unlike anything it had ever experienced or even imagined, let out a terrible roar.

—You bastard!

*Whoooooosh!*

A terrifyingly powerful Fear spread outward from Leviathan.

Marine creatures crouching in the deep sea rolled their eyes back and floated upward, while countless birds fleeing far away after sensing the danger that was about to arrive suddenly fell from the sky.

At this moment, Leviathan was angrier than it had ever been.

*I’ll kill them. I must!*

It had to tear them apart so completely that no one would be able to recognize them.

The human bastard who had inflicted this pain upon it and the traitor who had betrayed its own kind both deserved the most horrible deaths.

But within the emotions of pain and anger dominating Leviathan, fear suddenly raised its head.

*But how?*

The enemies had not only inflicted such a massive wound upon it the day before—they had deceived its senses and lured it into a trap.

And that human in particular…

That tiny creature that had dared to drive a weapon into its head possessed a power Leviathan could not understand at all.

*Strong. Stronger than any human I have ever seen.*

This would have been unimaginable during the Great Cataclysm.

Leviathan had roamed the five oceans, sending countless lives to watery graves. Even the humans considered the strongest had failed every time they tried to hunt it.

No.

Leviathan had always been the one doing the hunting.

It had been born a ruler and lived as a predator.

In this vast ocean, it had always been the predator, while humans were nothing more than prey that could be swallowed in a single bite.

Even after looking back across its distant lifetime, Leviathan could remember only one being who had ever made it submit.

The master to whom it had sworn loyalty.

The Demon King, Asmodeus.

—…!

In that instant, Leviathan’s eyes, stained with pain and anger, opened wide.

*Could this bastard be…?*

It had definitely heard of him before.

Of a human who had opposed its once-mighty master.

Though Leviathan had never once encountered that human, he had proven his strength by defeating countless monsters, ending with the great name of the Demon King Asmodeus.

*Then could this human really be…?*

There was no mistaking it.

There could not be two humans this strong.

Leviathan’s misunderstanding swelled into fear.

Before it knew it, the anger had disappeared, replaced by a single thought.

*I have to run. As far away as possible. I have to get away from him!*

Anger? Fighting spirit?

None of that mattered. If this human had defeated the Demon King Asmodeus, whom Leviathan had served as its master, then its own fate was practically decided.

—GROOOOOOAR!

Leviathan let out a massive roar and shook its body.

Its movements, no longer driven by pain but by the struggle to survive, were more violent than ever. But they had no effect on the figure who had already made a nest on its enormous body.

“Shut up. Shut up. Aren’t you going to shut up?”

*Bam! Bam! Bam!*

Blood splattered and flesh was crushed.

Under his tremendous grip, the incredibly tough scales were yanked out like cabbages, while the flames riding his punches crushed flesh and bone.

*Thud. Crack!*

—Kuhk. Khk.

The successive waves of pain nearly drove Leviathan unconscious.

The strength was so immense that it was impossible to imagine its wielder as human.

In the end, only one path remained.

The deep sea.

The place where Leviathan had first opened its eyes. An unknown domain deep beneath the ocean that no enemy had ever been able to invade.

If it reached that place, even this tenacious and terrifying human would be shaken off.

*Whoosh!*

Spray surged upward.

Leaving the shallow waters and advancing into the open sea, Leviathan swam deeper.

Then, the next moment, it saw the smiling face of the human and realized that its guess had been wrong.

“Now we can finally fight together.”

What?

A single question flashed through Leviathan’s mind.

At that moment—

*Whoooooosh!*

Deep within the abyssal darkness of the seawater, countless things gathered into one and blocked Leviathan’s path.

Bones.

They were bones.
```
