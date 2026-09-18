<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0406.txt",
      "sha256": "4c35ea64d9a332420a2ecbcd8b8cf554a680cfd2e005bbe70e6c339ea7696526",
      "bytes": 12997
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "debd493ad7a45ca2df17c29eee0c3afaa95ec5747af619e78771b669da4f763e",
      "bytes": 2216
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0040285ef821a0c0ec9425edcdd556ecefd458023cf6aba445c72f0efd0795c5",
      "bytes": 136172
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "6a9406d414f4861d7685f94fcc8e38ff75cd8e5adf4c8313b7d5ae4d43c7cbdf",
      "bytes": 590
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2a9bc023b858503dac3117d1ef05659b8d7fb7d23382c0ae96ae49f2f96773c1",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "aedad5150240cbf7c812a8b06bba107e5388e30abef6670223f697868923caf6",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "5ffc104caba2d55ea6ea66ca0f9ce7042b6a921cc8caeb5a7b132dd36e713960",
      "bytes": 1163
    },
    {
      "path": "characters/Seong Jinho.md",
      "sha256": "daf6112545777d3750b1b40a04cfd5981e92e0ea5fa629cec3294ed7451a7510",
      "bytes": 2186
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "b09ce2aef9bc2f818341e291fbf7242eb2e680f33e609d9cc83aa6d10ed3b736",
      "bytes": 560
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "21f6b99b4e2a3bd975cfc1bcd00524ce6f21d843ea306de42297920aabff34d6",
      "bytes": 119971
    }
  ],
  "estimated_tokens": 10566
}
-->

# Durable State Update — Chapter 406

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 406. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 406. Profile updates may replace only one
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
  "chapter": 406,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 406,
    "continuity_sources": [406],
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
    "The five fronts will begin mobile warfare at 06:30 the following morning, then cut off the monster army's retreat and establish a dense encirclement.",
    "Suining City in Sichuan Province is the operation's final destination and the place where the Arch Lich is located.",
    "Lee Jungryong sees China's devastation as an opening for Ares Guild and considers Jin Taekyung's growing heroic reputation dangerous.",
    "Go Jun has gained strength, defeated two Death Knights at the northern front, and remains Lee Jungryong's disciple and Head of Security.",
    "Lieutenant General Wang Ochun has become the northern-front commander after his predecessor's death and has maintained covert meetings with Go Jun at hidden safe houses.",
    "Ares Guild suffered eleven severely injured and forty-six lightly injured personnel on the northern front, with no deaths.",
    "Team Leader Choi and Shao Shen remain behind to recover because neither is currently fit for the departing operation.",
    "Hero's Soul did not reject Shao Shen when he gripped its hilt; Shao Shen judged Team Leader Choi more suitable and insisted that Choi receive it.",
    "Jin Taekyung has departed with the assembled forces for the operation intended to reach the Arch Lich."
  ],
  "continuity_sources": [
    405,
    404
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Will Jin and the assembled forces defeat the Arch Lich and end the war?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 405,
  "temporary_decisions": [
    "Render 영웅의 혼 as Hero's Soul and 영웅의 힘 as Hero's Power.",
    "Render 기동전 as mobile warfare.",
    "Render 쑤이닝시 as Suining City.",
    "Render 연대장 쉔 as Regimental Commander Shen.",
    "Render 진 선생 and 진 선생님 as Mr. Jin while preserving Jin's blunt, profane voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 장비               | **Equipment**                  |
| 로그인              | **Login**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 성진호 | **Seong Jinho** |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 탈주 | **Escape** | Song associated with Won Myunghoon. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 힐링 | **Healing** | Healing spell cast by Song Song. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 제로빅 | **Zerobic** | Name used in a forum joke about the recommended web novel. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 대통령 | **President** | Title for Korea's head of state. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 쑤이닝시 | **Suining City** | City in Sichuan Province and the operation's final destination. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 성진호 | junior_to_older_friend | Jinho | casual-but-junior | Spoken 형 may stay hyung; narration uses Jinho. Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 웨이펑후 | 이정룡 | senior military official to senior foreign S-rank Hunter | Mr. Lee | formal and concerned | Wei asks Lee whether something is wrong. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 394
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 405
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 405
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 405
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Seong Jinho.md

# Seong Jinho (성진호)

- **Safe through:** Chapter 206
- **Aliases:** Jinho; Mr. Seong Jinho
- **Role:** Manager of Hope Goshiwon; thirty-year-old exam candidate; civilian and Taekyung’s older friend who secretly rode inside Taekyung’s capsule after a college friend stole his housing deposit and now plans to live with him in the Guild-provided officetel
- **Personality:** Knowledgeable about IT, shamelessly blunt, melodramatic when threatened, and a heavy drinker
- **Voice:** Casual and teasing; invokes laws and hierarchy for comic effect; speaks informally to Taekyung while demanding respect as his older brother
- **Relationships:** Three years older than Jin Taekyung; treats him as a younger brother and drinking companion

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 405
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son; after Lei Fei’s death, he entrusted Lei Fei’s sword to Jin Taekyung.

## Korean source

```text
＃406화



마왕 아스모데우스의 강림으로 시작된 대격변의 시대는 음울하고 혼란했으나, 위기를 넘긴 인류는 빠르게 피해를 복구하고 전보다 더 수준 높은 문명을 이룩했다.

하지만 누군가에게는 마력석을 이용한 엘리베이터라든지, 힐링 포션 따위보다 더 중요한 것이 있기 마련이다.

“바로 인터넷이 빨라졌다는 거지.”

경건한 목소리로 중얼거린 남자는 안경을 추켜올렸다.

현재 시각 오전 열한 시 삼십 분. 그의 등 뒤에서는 막 투입된 라면이 자글자글 끓었고, 식탁에는 식은 밥과 신김치가 세팅되어 있었다.

모든 준비는 끝났다. 정확히 3분 후, 마트 세일 당시 고민 끝에 구매한 A급 특란을 한 개, 아니 두 개 넣은 다음 2분만 더 기다리면 완벽한 점심이 완성된다.

그리고 그때까지의 지루함은 스마트폰이라는 경이로운 현대 문명이 해결해 줄 것이다.

“어디이 보자아, 오늘 기사가아…….”

남자는 흥얼거리며 스마트폰 화면을 훑었다.

그가 자주 들르는 대형 포럼 사이트, ‘헌터 대학’의 메인에는 새로운 베스트 글이 순위에 따라 업데이트되어 있었다.



1위. [연이은 승전보, 이미 와해된 것이 다름없는 몬스터 군단? 유엔 안보리 공식 입장 표명. “인류는 강하다. 그러나 아직 전쟁은 끝나지 않았다. 마지막까지 방심은 금물.”]

2위. [쓰촨성의 기적. 그날, 그곳의 중심에 진태경이 있었다.]

3위. [나날이 올라가는 국격, 새로운 영웅의 탄생. K-POP, 김치 판매량 급증.]

4위. [예정된 한미 정상회담 진행…… 美 대통령 도람프 공식 석상서 파격 발언, “이곳이 진태경의 나라입니까? 그는 내 우상입니다.”]

5위. [연전연승을 거듭하는 아레스 길드. 과연 명불허전.]

6위. [샤오 양 중국 주석, “그들 모두가 영웅이다.”]

7위. [매생이 닷컴 번역, 현 상황에 대한 해외 네티즌들의 반응. “도대체 코리안들이 틈만 나면 죽여 대는 주모(Jumo)가 누구야?”]

8위. [日 총리 마이구미 신지로, “몬스터 웨이브는 Fun하고 Cool하고 Sexy하게 대처해야 한다.” 무슨 뜻이냐고 묻는 기자의 질문에 씩 웃으며, “그걸 설명하는 것 자체가 섹시하지 않다.”]

9위. [러시아 대통령 푸린, “내게 있어 신지로는 양자역학 같은 사람이다. 아무리 봐도 이해할 수가 없다.”]

10위. [예언자가 된 웹소설 작가, 제로빅 전격 인터뷰. “지금 심정? 얼떨떨하다. 그런 김에 오늘은 휴재하겠다.” 인터뷰 도중 분노한 담당 편집자의 난입에 전치 12주 부상. 뜻하지 않은 휴재. 그러나 피를 흘리면서도 쉴 수 있게 되어 기쁘다며 웃는 제로빅, 담당 편집자 이 모 씨의 눈물, “사람 새끼가 아니다.”]

.

.

.



“이야. 아주 난리도 아니구만. 난리도 아냐.”

중얼거리는 남자의 입가에는 미소가 맺혀 있었다. 스크롤을 쭉쭉 내려봐도 온통 진태경에 관한 이야기뿐이었다.

중간중간 이상한 내용의 기사들이 섞여 있는 것 같긴 하지만, 보는 것만으로도 가슴 깊숙한 곳에서 뿌듯함이 차올랐다.

이미 댓글 창은 폭발 직전이다.



요즘 화력 미쳤네. 헌터 대학 초딩 때부터 했지만 이렇게까지 달아오른 건 처음 본다;;

└ 진짜 미친 건 진태경임. 혼자서 일만의 몬스터 군단을 썰어 버렸자너. 다시 생각해도 어이없네. 어떻게 그게 되지?

└ 대단하긴 한데 말은 똑바로 하자. 일만이 아니라 몇천 마리 정도임.

└ ㅋㅋㅋㅋㅋㅋㅋ그것도 미친 건 매한가지 아니냐?

└ ㄹㅇㅋㅋㅋㅋ엉덩이에 고블린 독침 맞으면 아앗 살살 놔 주세요 할 새끼가; 너 지난번에 키보드로 오러 블레이드 쓰던 그 새끼지?



근데 이 정도면 진태경은 그냥 S급 헌터가 아닌 것 같은데? 다른 S급 헌터들도 다 저럼?

└ 대격변 당시에도 이 정도 전공은 드물었지; 천태민은 뭐 하도 넘사벽이니까 제외하고…… 당장 대격변 당시 기록지 보면 이정룡도 비슷한 전공 세운 적 있을걸?

└ 흠. 아직 이정룡 급은 아닌 건가? 실망이네.

└ ?? 이정룡이 무슨 동네 뒷산 약수터 할아버지로 보이냐? 천태민에 가려져서 그렇지 지금까지 세운 전공이나 보여 준 무력, 영향력으로는 전 세계에서 손꼽히는 탑 클래스임;

└ 222. 일주일 전만 봐도 답 나옴. 다섯 개 전선 통틀어서 가장 적은 피해로 몬스터 군단 박살 냈잖아. 진태경도 대단하지만 이정룡이랑 아레스 길드도 개쩜. 지금 진군하는 속도도 북부 전선이 좀 더 빠름.

└ 이런 댓글 보면 괜히 불안해지더라. 또 생각 없는 애들 달려와서 vs질 오지게 할까 봐.

└ 아이피 차단 오지게 먹여서 괜찮을걸. 근데 이 정도면 사실상 이번 사태 끝난 거 아니냐? 지금 기동전으로 몬스터들 개박살 내고 있잖아.

└ 일주일 동안 전승무패 ㄷㄷㄷ;

└ 아크 리치도 당황했을 듯. 일주일 전에 힘 빡 주고 기습했는데 다 털려 버려서. 데스나이트 로드도 죽었지, 살아남아서 도망친 놈들은 지금 추수당하고 있어서 노답임.



이쯤 되면 아크 리치가 나서야 하는 거 아님? 너무 조용하니까 이상한데.

└ 나도 그 생각 들어서 어제 안부 인사 겸 카톡 해 봄.

└ ? 누구한테?

└ 아크 리치. 지금 승급전이라 바쁘다던데. 이번 판만 이기면 골드 간다고 좋아하더라.

└ 윗 댓글 미친놈이네.

└ 더 미친놈은 제로빅이지. 작가 새끼 갑자기 왜 휴재함? 물 들어올 때 노 저어야지, 어이없네.

└ 개소리들 그만하고 지금 중요한 건 이대로만 가면 더 이상 큰 피해 없이 이번 몬스터 웨이브 진압할 수 있다는 거다. 조속히 사태가 마무리되길 기도하면서, 희생된 피해자들을 위해 묵념하자.

└ 음…… 중국 싫어하긴 하는데 ㅇㅈ함. 어느 나라에나 병신과 정상인은 공존하는 법이니까. 헌터, 군인들 모두 ㅎㅇㅌ.

└ 화이팅.



네티즌들의 분위기는 전체적으로 화기애애했다.

초기에는 심각하게 받아들여졌던 몬스터 웨이브는 이제 국뽕의 소재로 활용되고 있었고, 희생자들을 애도하며 응원하는 댓글에서는 두려움 대신 희망이 느껴졌다.

‘하긴, 요즘 들어서 희소식이 많이 들려오긴 하지.’

남자는 고개를 끄덕였다. 그럴 만도 했다. 유엔 안보리가 전하는 전황에 따르면 이미 승기는 훌쩍 기운 것이 틀림없었으니까.

일주일 전, 다섯 개 전선을 목표로 일거에 들이친 기습은 큰 피해를 낳았지만, 사상자를 훨씬 웃도는 증원군이 파견되었고 그 후는 승리의 연속이었다.

‘이 정도 속도라면 며칠 안에 끝날지도.’

그야말로 파죽지세(破竹之勢). 그중에서도 가장 두드러지는 것은 진태경이 맡은 서부 전선과 이정룡이 이끄는 북부 전선이었다.

‘짜식. 처음에는 많이 걱정했었는데, 생각보다 더 잘하고 있네.’

잠시 고민하던 남자는 사이트에 로그인하여 댓글을 남겼다.



진태경 동거인 : 그 찐따 같던 진태경이 맞나? 진짜 진태경은 전설이다. 진짜 옛날에 맨날 같이 라면 먹었는데 왕 같은 존재인 S급 헌터가 돼서 세계최강 전설적인 영웅이 된 진태경을 보면 진짜 내가 다 감격스럽다…….



댓글을 달기가 무섭게 대댓글이 우후죽순으로 달리기 시작한다.

흐뭇한 얼굴로 휴대폰을 바라보던 남자, 성진호는 문득 중요한 사실을 잊고 있었음을 깨달았다.

“안 돼! 내 라면!”



* * *



“아, 라면 땡기네.”

내 중얼거림에 옆에 있던 최 팀장이 물었다. 회복을 끝마친 그는 어젯밤, 제트기를 타고 전선에 합류했다.

“갑자기 말입니까?”

“그러게요. 이상하네.”

“상황이 상황인지라 진태경 씨가 더 대단해 보이는군요.”

서걱!

빛살처럼 휘둘려진 [영웅의 혼]이 리자드 맨의 무기와 몸뚱어리를 동시에 베었다.

쏟아지는 녹색 핏물과 코를 찌르는 악취. 나는 식욕이 뚝 떨어지는 것을 느끼며 몸을 날렸다.

쐐애애애액, 콰아아!

멸염신권(滅炎神拳).

끔찍한 열기가 수십 마리의 리자드 맨을 휘감고 타오른다. 그 광경에 주춤거리는 몬스터들의 모습은 이미 패잔병의 그것이나 다름없다.

흐름을 읽은 샤오 쉔이 선두로 달려나가며 외쳤다.

「돌격! 돌격하라!」

「와아아아아-!」

「바람의 칼날이여, 이곳에 임하소서! 윈드 커터(Wind Cutter)!」

쉬쉬쉬쉬쉭!

카카캉! 서걱!

- 쿠에에엑!

- 키룩, 컥!

파도처럼 쏟아지는 인간의 공세에 몬스터들은 속수무책으로 밀렸다.

머릿수는 비등하지만 사기와 병력의 질에서 상대가 안 되는 싸움.

일선이 모래성처럼 허물어지자 잔뜩 겁에 질린 몇몇 놈들이 등을 돌려 도망치기 시작한다.

‘그리고 붕괴는 한순간이지.’

두려움은 전염되는 법.

하나가 도망치면 열이 따르고, 그 후에는 걷잡을 수 없는 탈주극이 벌어진다.

아니나 다를까, 내 예상은 정확히 맞아떨어졌고 이내 승리를 확신하는 외침이 들려왔다.

「추격하라! 한 놈도 살려 보내서는 안 된다!」

「빨리 속도 버프 걸어!」

「원거리 부대! 준비, 쏴!」

쉬쉬쉭! 퍼벙!

한껏 기세가 오른 헌터들은 대열도 갖추지 않고 도망치는 몬스터들을 학살하기 시작했다.

약 한 달 전만 하더라도 자동차로 가득했을 6차선 아스팔트 도로가 몬스터들의 사체로 메워지기까지는 그리 오랜 시간이 필요하지 않았다.

“또 승리했군요.”

전투가 끝난 후, 장비를 점검하고 있던 나는 말을 건네오는 최 팀장을 보며 어깨를 으쓱했다.

“좋은 소식을 전하는 것치곤 표정이 영 아니신데요?”

“그거 묘하네요. 저도 막 진태경 씨를 보면서 그런 생각을 했지 뭡니까.”

“……흠.”

아마 서로 비슷한 생각을 하고 있던 모양이다.

그의 말마따나 나는 승리했음에도 전혀 기쁘지 않다.

지금과 같은 이질감을 느낀 것은 본격적인 반격을 위해 기동전을 시작하고 이틀째 되던 날부터였다.

“최 팀장님 생각은 어떠세요?”

“어떤 것을 물으시는 겁니까? 몬스터의 숫자와 질이 크게 줄어든 것? 아니면 지난 일주일간 거두신 수십 번의 승리?”

“둘 다죠.”

“아마 지금 진태경 씨가 생각하고 계시는 것과 동일할 겁니다. 분명히 현재의 전황은 고무적이지만…… 뭔가 꺼림칙해요.”

최 팀장은 환호하는 사람들을 바라보았다.

지친 얼굴에 번진 웃음. 곧 전쟁을 끝내고 사랑하는 이들의 품으로 돌아갈 수 있다는 희망에 가득 찬 미소였다.

“이해가 안 되는 것은 아닙니다. 개전 초기에 등장했던 상위 몬스터가 워낙 많았으니까요. 정예 병력을 손실했다면 지금과 같은 상황이 벌어질 수 있죠. 하지만…….”

“아크 리치. 그놈이 이렇게 호락호락할 리가 없다는 게 문제지. 안 그렇습니까, 최 팀장님?”

작게 고개를 끄덕인 최 팀장이 물었다.

“상부에서도 저희와 같은 생각을 하고 있습니까?”

“아마도. 다른 S급 헌터들은 몰라도 웨이펑후 국방부장은 정확히 인지하고 있더군요.”

“그렇다면 다행이지만…….”

최 팀장은 말꼬리를 흐렸다. 아마 이번 역시 그도 나와 같은 생각을 떠올렸을 것이다.

이제 목적지인 쑤이닝시까지는 코앞이나 다름없는 상황.

전쟁이 계속되는 내내 한 번도 모습을 나타내지 않은 아크 리치는 도대체 지금쯤 뭘 하고 있을까?

- 음. 지금쯤이면 뼈에 기름을 바르고 있을 시간이지. 멋진 언데드가 되기 위해서는 관리가 필요하거든.

“…….”

닥쳐 좀.



* * *



쏴아아아악.

드넓은 공간. 소용돌이치던 어둠이 어딘가를 향해 빨려 들어간다.

칠흑빛 어둠이 사라지고 깨져 나간 유리창 사이로 흘러들어온 노을빛이 한 존재에 닿았다.

- 오라, 대적자여.

겨울바람처럼 서늘한 목소리. 마력을 갈무리한 아크 리치는 안광을 빛냈다.
```

## Final English reading copy

```markdown
# Chapter 406

The era of upheaval that began with the descent of Asmodeus, the Demon King, had been grim and chaotic. But after overcoming the crisis, humanity quickly repaired the damage and built a civilization even more advanced than before.

Still, for some people, there were things more important than elevators powered by mana stones or healing potions.

“The internet got faster.”

The man who muttered those words in a reverent voice adjusted his glasses.

It was 11:30 a.m. Behind him, the ramen he had just added to the pot was bubbling away, while cold rice and sour kimchi had been laid out on the table.

Everything was ready. In exactly three minutes, he would add one—no, two—A-grade jumbo eggs he had agonized over before buying during a supermarket sale. After waiting two more minutes, the perfect lunch would be complete.

And until then, the boredom would be solved by the marvelous modern civilization known as the smartphone.

“Let’s see what we have here… Today’s news…”

Humming, the man skimmed through his smartphone screen.

The main page of *Hunter University*, a large online forum he visited often, displayed new best posts ranked by popularity.

1. **[Victory report after victory report—is the monster army already as good as shattered? The UN Security Council issues an official statement: “Humanity is strong. But the war is not over yet. We must not let our guard down until the very end.”]**

2. **[The Miracle of Sichuan Province. Jin Taekyung stood at the center of it all.]**

3. **[National prestige rises by the day as a new hero is born. K-pop and kimchi sales skyrocket.]**

4. **[Scheduled Korea–US summit to proceed… President Doramp makes a startling statement at an official event: “Is this Jin Taekyung’s country? He’s my idol.”]**

5. **[Ares Guild continues its string of victories. Truly living up to its reputation.]**

6. **[Chinese Chairman Xiao Yang: “Every one of them is a hero.”]**

7. **[Maesaeng-i.com Translation: Overseas netizens react to the current situation. “Who the hell is this ‘Lady of the House’ Koreans keep killing every chance they get?”]**

8. **[Japanese Prime Minister Maigumi Shinjiro: “Monster waves must be handled in a Fun, Cool, and Sexy manner.” When a reporter asked what that meant, he grinned and replied, “Explaining it wouldn’t be sexy.”]**

9. **[Russian President Furin: “To me, Shinjiro is like quantum mechanics. No matter how much I look at him, I can’t understand him.”]**

10. **[Web-novel author becomes a prophet: exclusive interview with Zerobic. “How do I feel right now? I’m still stunned. Since we’re on the subject, I’ll be taking a break today.” During the interview, his enraged editor burst in and injured him badly enough to require twelve weeks of treatment, resulting in an unexpected hiatus. Zerobic smiled and said he was happy to be able to rest despite bleeding, while editor Mr. Lee shed tears and said, “He isn’t human.”]**

.

.

.

“Wow. This place is absolutely insane. Completely insane.”

A smile spread across the muttering man’s lips. No matter how far he scrolled, everything was about Jin Taekyung.

Some strange articles seemed to be mixed in here and there, but simply looking at them made a deep sense of pride well up inside his chest.

The comment section was already on the verge of exploding.

> The activity here is insane lately. I’ve been on Hunter University since elementary school, but I’ve never seen it this heated before;;

> └ The truly insane one is Jin Taekyung. He carved through a monster army ten thousand strong all by himself. It still makes no sense when I think about it. How the hell did he do that?

> └ He’s amazing, but let’s get the facts straight. It wasn’t ten thousand, it was a few thousand at most.

> └ LMAOOOO isn’t that still completely insane?

> └ For realㅋㅋㅋㅋ You’re the kind of bastard who’d get a goblin’s poison stinger in the ass and yell, “Ow, please let go gently!” Aren’t you the same guy who used an aura blade with your keyboard last time?

> But at this point, Jin Taekyung doesn’t seem like an ordinary S-rank Hunter. Are all the other S-rank Hunters like that too?

> └ Even during the Great Cataclysm, feats on this level were rare. Cheon Taemin doesn’t count because he was just on another level entirely… But if you look at the records from the Great Cataclysm, Lee Jungryong probably accomplished something similar too.

> └ Hmm. So he still isn’t at Lee Jungryong’s level? Disappointing.

> └ ?? Do you think Lee Jungryong is some old man at a spring on a hill behind the neighborhood? He may be overshadowed by Cheon Taemin, but based on his achievements, martial power, and influence, he’s one of the top-class figures in the entire world.

> └ 222. You only have to look at what happened a week ago. He wiped out the monster army with the fewest casualties across all five fronts. Jin Taekyung is incredible, but Lee Jungryong and Ares Guild are fucking amazing too. The northern front is actually advancing a little faster right now.

> └ Comments like this make me nervous for no reason. I’m worried that a bunch of idiots will show up again and start going wild with the versus arguments.

> └ They’ve been IP-banned to hell, so it should be fine. But at this point, isn’t the whole incident basically over? They’re crushing the monsters through mobile warfare right now.

> └ Undefeated for an entire week ㄷㄷㄷ;

> └ The Arch Lich must have been caught off guard. It went all-out with a surprise attack a week ago and got completely wrecked. The Death Knight Lord is dead, and the ones who survived and ran away are being hunted down now. No chance for them.

> At this point, shouldn’t the Arch Lich be making a move? It’s so quiet that it feels strange.

> └ I had the same thought, so I sent it a KakaoTalk message yesterday as a friendly check-in.

> └ ? To whom?

> └ The Arch Lich. It said it was busy with its promotion match. Apparently, it was excited because winning this game would get it to Gold.

> └ The guy above is fucking insane.

> └ Zerobic is even more insane. Why the hell is that author suddenly taking a break? You have to row when the tide comes in, you idiot.

> └ Stop talking bullshit. The important thing is that if things continue like this, we can suppress this monster wave without suffering any more major losses. Let’s pray that the situation ends soon, then observe a moment of silence for the victims who were sacrificed.

> └ Hmm… I don’t like China, but I agree with this one. Idiots and normal people coexist in every country. Good luck to all the Hunters and soldiers.

> └ Fighting.

The netizens were generally in a cheerful mood.

The monster wave, which had initially been viewed with deadly seriousness, had now become material for nationalistic pride. Even in the comments mourning the dead and cheering on those fighting, there was hope instead of fear.

*Then again, we have been hearing a lot of good news lately.*

The man nodded. It was only natural. According to the battlefield reports from the UN Security Council, there was no doubt that the tide had already turned decisively.

A week ago, the surprise attack launched simultaneously against all five fronts had caused enormous damage. But reinforcements far exceeding the number of casualties had been dispatched, and victory after victory had followed.

*At this rate, it might be over in a few days.*

Their momentum was unstoppable, like splitting bamboo. The western front under Jin Taekyung and the northern front led by Lee Jungryong stood out the most.

*The little punk. I was so worried about him at first, but he’s doing even better than I expected.*

After hesitating for a moment, the man logged into the site and left a comment.

> **Jin Taekyung’s Roommate:** Is that pathetic Jin Taekyung really him? The real Jin Taekyung is a legend. I used to eat ramen with him all the time back in the day, and now he’s become an S-rank Hunter, a king-like figure, and the world’s strongest legendary hero. When I look at him, I’m genuinely moved…

The moment he posted the comment, replies began springing up one after another.

The man gazed at his phone with a pleased expression.

Then Seong Jinho suddenly realized he had forgotten something important.

“No! My ramen!”

* * *

“Man, I could really go for some ramen.”

At my mutter, Team Leader Choi, who was standing beside me, asked a question. After finishing his recovery, he had flown to the front on a jet the previous night.

“Out of nowhere?”

“Yeah. Weird, isn’t it?”

“Given the situation, it makes you seem even more impressive, Mr. Jin.”

Swish!

Hero’s Soul, swung like a streak of light, sliced through both the lizard man’s weapon and its body.

Green blood poured out, accompanied by a stench that stabbed straight into my nose. Feeling my appetite vanish completely, I launched myself forward.

Fwoooosh! Boom!

“Flame-Extinguishing Divine Fist.”

Horrific heat coiled around dozens of lizard men and erupted into flames. The monsters hesitating at the sight were already no different from a defeated army.

Shao Shen read the flow of battle and charged to the front, shouting.

“Charge! Charge!”

“Waaaaaah!”

“Blade of the wind, descend upon this place! Wind Cutter!”

Shwish-shwish-shwish-shwish!

Clang! Slash!

—Kueeeek!

—Kiruk, krk!

Overwhelmed by the human offensive pouring down like a wave, the monsters were helplessly driven back.

The numbers were roughly even, but it was a battle the monsters could not possibly win in terms of morale or the quality of their forces.

Once the front line collapsed like a sandcastle, several terrified monsters turned their backs and began to flee.

*And collapse happens in an instant.*

Fear was contagious.

When one fled, ten followed. After that, an uncontrollable rout began.

Sure enough, my prediction proved accurate, and before long, cries of certain victory rang out.

“Pursue them! Don’t let a single one survive!”

“Get the speed buffs up!”

“Ranged units! Ready—fire!”

Shwish-shwish! Boom!

The Hunters, their momentum at its peak, began slaughtering the monsters fleeing without even maintaining formation.

It did not take long for the six-lane asphalt road, which would have been packed with cars only a month ago, to become buried beneath monster corpses.

“We won again.”

After the battle, I was checking my equipment when Team Leader Choi approached me. I shrugged.

“For someone delivering good news, you don’t look very happy.”

“That’s strange. I was just thinking the same thing while looking at you, Mr. Jin.”

“……Hmm.”

Apparently, we had been thinking along similar lines.

As he said, I was not happy at all, despite our victory.

I had first begun feeling this same sense of incongruity on the second day after we launched our mobile warfare as part of the full-scale counterattack.

“What do you think, Team Leader Choi?”

“What exactly are you asking about? The fact that the number and quality of the monsters have declined so sharply? Or the dozens of victories you’ve achieved over the past week?”

“Both.”

“You’re probably thinking exactly what I am. The current state of the war is certainly encouraging, but… something feels wrong.”

Team Leader Choi looked toward the people celebrating.

Smiles spread across exhausted faces. They were filled with hope—the hope that they would soon end the war and return to the arms of their loved ones.

“It’s not as if I don’t understand. There were so many high-level monsters during the early stages of the war. If the elite forces suffered heavy losses, a situation like this could happen. But…”

“The Arch Lich. That bastard wouldn’t go down this easily. Would it, Team Leader Choi?”

Team Leader Choi gave a small nod before asking,

“Do the higher-ups share our thoughts?”

“Probably. I don’t know about the other S-rank Hunters, but Minister of National Defense Wei Fenghu understood the situation perfectly.”

“That’s a relief, but…”

Team Leader Choi let his voice trail off. He had probably thought of the same thing I had this time as well.

We were practically at our destination, Suining City.

The Arch Lich had not shown itself even once throughout the war. What on earth was it doing right now?

—Hmm. At this point, it should be time to grease its bones. Becoming a magnificent undead requires proper maintenance, you know.

“……”

*Shut up.*

* * *

Swoosh.

A vast space.

The darkness swirling within it was sucked toward somewhere.

The pitch-black darkness vanished, and the light of the setting sun, filtering through shattered windows, touched a single being.

—Come, adversary.

His voice was as cold as the winter wind.

Having gathered its mana, the Arch Lich’s eyes gleamed.
```
