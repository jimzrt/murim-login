<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0828.txt",
      "sha256": "1ee5626532fbd0f8ce19ac0b6f52e682c5c22f1c586e3afa3d5fba8974adee8c",
      "bytes": 15141
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7ad761bb24952b04a20813546b3a5e97f7102b0f6bee2dcffa8c1ddf411b61f1",
      "bytes": 1758
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3c3b9627e7353c69a66f8e10657ef055c79a30700111295e071d564e07f7e0ae",
      "bytes": 226707
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6e23d6589facf27845b568569efba509616ec37a060434d96cd65d9c52fc0ec3",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "c51a8d36e9e0bcc4fba423abdcbb1b8c47c0705891cba74096761caa61a398ae",
      "bytes": 872
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "76db88858d8417ded86764cb1f62df01b4ce362f57c2f73253088c5ca71c2542",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0909ab38829e13de23172a03602b29dd9ac928d8a4df42b765797335e275dedc",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "67c773e1faecc341a7cfdee91a1ed0aa8d8bc470d8ce806fc6749e013e6e32b8",
      "bytes": 250673
    }
  ],
  "estimated_tokens": 10673
}
-->

# Durable State Update — Chapter 828

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 828. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 828. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 828,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 828,
    "continuity_sources": [828],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Doppelganger known as The Prophet.",
    "The Doppelganger is the last surviving member of its species and can absorb appearances, abilities, and memories; it currently has Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger claims to have served Demon King Asmodeus and received his order to infiltrate humanity before Asmodeus fell.",
    "The Doppelganger says the temple’s empty throne was made for the Great King and that Asmodeus will return with his armies.",
    "Jin believes Asmodeus died on Victory Day, the day Jin was born, but cannot yet determine whether the Doppelganger’s claims are true.",
    "Jin destroyed the temple’s seventy-two stone constructs and magic circles using White Flame controlled by his Middle Dantian.",
    "A dazzling radiance filled the temple after Jin challenged the Doppelganger; its source and what followed are unknown."
  ],
  "continuity_sources": [
    826,
    827
  ],
  "open_questions": [
    "Is Demon King Asmodeus truly dead, and will he return?",
    "Are the Doppelganger’s claims about Asmodeus and the temple true?",
    "What caused the radiance that filled the temple?"
  ],
  "safe_through": 827,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword.”",
    "Render 에어 슬래시 as “Air Slash” and 실드 마법 as “Shield magic.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 경험치              | **EXP**                        |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 골렘 | **Golem** | Magical rock-based monster classification. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 바인딩 | **Binding** | A restraining spell used by the mage unit. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 기자 | 진태경 | Japanese reporter to celebrated foreign Hunter | Jin-sama | formal and reverent | Japanese reporters repeatedly address Jin with the honorific 사마. |
| 진태경 | 기자 | Hunter to Japanese reporter | reporter; you | blunt and insulting | Jin rebukes a reporter for talking back after criticizing Yamamoto's delayed arrival. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 827
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 827
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 827
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 827
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃828화



두려움에도 종류와 정도가 있다.

누군가는 어린 시절 계곡에 빠졌던 기억으로 평생을 물 공포증에 시달리고, 지진을 겪은 이들은 낙인과도 같은 트라우마를 안고 살아간다.

하지만 그중에서도 가장 크고 깊은 것은 바로 미지에 대한 두려움이다.

지금껏 누구도 본 적 없는, 혹은 상상할 수도 없는 영역.

미지(未知)란 그런 것이다.

과학과 마법으로 찬란한 문명을 꽃피운 인류조차 완전히 닿지 못한 우주, 심해.

그리고 지금 이 순간, 온 사방을 찢어발기는 저 한 줄기의 불꽃과 같은.

콰아아아!

그것은 마치 폭풍 같았다.

소름 끼칠 정도로 예리하고, 닿는 것만으로도 모든 것을 잿더미로 만들어 버리는 불의 폭풍.

도플갱어는 아연한 시선으로 그 광경을 바라보았다.

숨 막히는 열기를 뿜어내는 청백색의 화염이, 그의 두 눈동자를 불그스름하게 물들이고 있었다.

슈화악!

찢고, 가르고, 벤다.

바람이 날카로운 비명을 내질렀다. 지난 삼 년간 공들여 빚어 낸 골렘(Golem)들이 폭죽처럼 터져 나갔다.

거대하고 단단한 암석으로 이루어진 팔다리도, 대지를 가르며 내려 찍은 무기도 소용없었다.

화륵, 콰드드득!

녹아내린다. 부서진다.

자그마치 일흔두 기에 달하는 골렘이 그저 한낱 돌무더기가 되기까지 걸린 시간은 찰나에 불과했고, 그건 도플갱어가 후퇴 명령을 내리기도 전에 벌어진 일이었다.

아니, 그럴 여유조차 없었다는 것이 더 옳은 표현이었다.

온 사방을 찢어발긴 화염에 의해 파괴된 것은, 비단 저 골렘뿐만이 아니었으니까.

콰창.

요동치는 거대한 기운.

휘황한 빛무리를 흩뿌리던 마법진들이 폭발하듯 터져 나갔다.

도플갱어는 자신의 주변을 둘러싼 반투명한 막이 촛농처럼 녹아내리는 것을 바라보며 경악했다.

“이게 무슨…….”

그러나 채 목소리가 이어지기도 전에, 신체 깊숙한 곳에서 울컥 솟구친 뜨거운 무언가가 목구멍을 타고 입안으로 흘러넘쳤다.

쿨럭.

검붉은 핏덩이를 토해 낸 도플갱어의 동공이 파르르 떨렸다.

지크프리트 바스만의 기억 속에서 떠오른 지식이 그의 텅 빈 머릿속을 후려쳤다.

마나 역류.

수많은 마법진과의 연결이 강제로 끊기자 전신의 기운이 들끓어 오른다.

만약 그가 여러 매개체와 술식을 통해 마법진을 준비하지 않고 직접 마법을 발현시켰다면, 몇 번을 죽었어도 이상하지 않을 심각한 타격이었다.

‘도대체, 도대체 어떻게?’

도플갱어는 숨을 헐떡이며 고개를 들었다.

경악으로 가득 찬 두 눈동자에는 더 이상 한 줌의 여유도 깃들어 있지 않았다.

그저 미지(未知)처럼 느껴지는 한 인간만이 선명히 비치고 있을 뿐.

‘진태경.’

그가 보인다.

새하얗게 빛나는 은빛 창을 쥔 채 머리 위로 쏟아지는 골렘들의 잔해 사이에 우뚝 서 있는 그가.

이내 화염에 의해 녹아내린 마법진이 남긴 빛무리 사이로, 자신을 응시하는 포식자의 모습이.

“다시 지껄여 봐.”

금방이라도 끊어질 것 같은, 그러나 용암처럼 들끓는 목소리가 도플갱어의 귓가를 파고든다.

금방이라도 쓰러질 것처럼 비틀거리는 발걸음이 그를 향해 다가온다.

저벅.

참으로 이상한 일이었다.

온 사방이 굉음으로 가득한데. 기둥을 잃은 신전이 서서히 허물어지고 한때 골렘이었던 암석들이 사방으로 비산하고 있는데…….

저벅.

저 작은 인간의 발걸음 소리가 천둥처럼 들린다는 것이. 뒤이어 들려온 그 목소리에 전신의 털이 곤두선다는 사실이.

“도대체 누가, 이곳의 주인이라고?”

“……!”

그 순간, 도플갱어는 자신도 모르게 입술 사이로 흘러나오려는 비명을 삼켜야 했다.

진태경을 바라보는 그의 눈동자에는 또렷한 공포가 아로새겨져 있었다.

괴물. 저 인간은 괴물이었다.

그것도 매번 예상과 한계를 아득히 뛰어넘는.

앞서 전장에서 무수한 죽음을 겪은 뒤, 진태경을 경시하던 마음을 이미 일찌감치 내버렸던 도플갱어다.

모든 것을 내려놓고 냉정하게 판단했다. 이번만큼은 확신할 수 있었다.

목적지에 다다르면 모든 것이 문제없이 흘러갈 것이라고.

진태경은 결코 자신을 잡을 수 없을 거라고.

그러나 아니었다.

누구보다 먼저 전장에서 이탈했던 도플갱어는 그 짧은 시간 동안 진태경이 더 높은 경지로 발돋움했다는 것을 몰랐다.

뒤늦게 그 사실을 깨달은 지금은 모든 것이 늦어 있었다.

‘여기서 조금이라도 더 시간을 지체한다면…… 그때는 정말 끝장이다.’

영원한 소멸.

머릿속을 스친 생각과 함께, 서늘한 공포가 등골을 타고 기어오른다.

동시에 이어진 움직임은 이성보다는 본능에 가까웠다.

도플갱어는 자신에게 남아 있는 영혼들을 아낌없이 불태웠다. 마나 역류로 엉망이 된 신체를 치유하고, 다시 충만하게 차오른 기운을 두 손에 담아 펼쳤다.

자신을 향해 다가오는 저 인간 같지 않은 괴물을 향해.

진태경을 향해.

화아악!

아득한 섬광이 터져 나온 그 순간.

“안 돼!”

그보다 한발 앞서 도플갱어를 향해 쇄도해 가던 스켈레톤 킹이 황급히 신형을 틀어 섬광의 앞을 가로막았다.

팟!

평소의 스켈레톤 킹이었다면 콧방귀조차 뀌지 않았을 것이다.

말로는 온갖 허풍을 떨어 대도, 진태경이 자신을 뛰어넘는 강자라는 것쯤은 인정하고 있었으니까.

하지만…….

‘지금 간악한 인간을 지킬 수 있는 건, 오직 이 몸뿐이다.’

지킨다. 설령 자신이 위험해지는 한이 있더라도.

스켈레톤 킹에게 있어 그것은 너무나도 당연한 일이 되었다.

이유?

그런 것 따위는 어느 날부터인가 생각하지 않았다. 친구 사이에는 어떤 이유도 없는 법이니까.

쏴악!

스켈레톤 킹은 [영웅의 검]을 내리그었다.

마력과는 도무지 어울리지 않는, 마치 햇빛처럼 환한 황금빛 마력이 섬광을 갈랐다.

아니.

갈랐다고 생각한 그 순간, 검신을 안개처럼 통과한 섬광이 풍선처럼 부풀었다.

후웅.

‘이게 무…….’

뇌리에 떠오른 의문이 끝맺어지기도 전에, 조금 전과는 비교도 되지 않는 빛이 스켈레톤 킹의 시야를 가득 채웠다.

화아아악!

온 세상이 새하얗게 물들었다.

평범한 인간이었다면 단번에 시력을 상실했을 그 아득한 섬광 속에서, 스켈레톤 킹은 뒤늦게 의문에 대한 답을 떠올렸다.

‘제기랄.’

틀림없다.

이건 중하급 정도의 마법사들도 손쉽게 발현시킨다는 라이트(Light) 마법이다.

그러나 살상력이 떨어지고 빛의 농도도 옅은 편이기에 실전에서는 거의 사용되지 않는, 단순한 편의성 마법.

적어도 스켈레톤 킹은 그렇게 알고 있었고, 헌터계에서는 정설(定說)처럼 받아들이는 내용이기도 했다.

만약 그가 지크프리트 바스만이라는 학구파 대마도사가 은신처에 틀어박힌 채 숱한 마법을 연구했으며, 그중 라이트 마법의 위력과 효용성을 몇 단계나 끌어올렸다는 사실을 알았다면 충분히 대처할 수 있었을 것이다.

그러나 이미 물은 엎질러졌고, 이 뼈아픈 실수는 스켈레톤 킹의 가슴을 덜컥 내려앉게 하기에 충분했다.

‘보이지 않는다. 아무것도.’

시력을 완전히 상실한 것은 아니었다.

스켈레톤 킹의 본질은 언데드고, 이는 피륙으로 이루어진 인간과는 비교할 수 없는 생명력을 지녔다는 뜻이니까.

하지만 도플갱어라는 강적과 맞서 싸우는 도중에, 그것도 다른 누군가를 보호해야 하는 상황에서 잠시나마 시력을 잃었다는 것은 돌이킬 수 없는 실수였다.

‘처음부터 이걸 노렸어. 내가 막아설 걸 알고…….’

아무것도 보이지 않는 새하얀 세상 속에서, 스켈레톤 킹은 검을 치켜세웠다. 시력의 상실과 함께 한껏 청각이 주위의 모든 상황을 받아들인다.

뒤늦게 떨어진 돌무더기로 인한 굉음.

저 허공 위에서 들려오는 알 수 없는 금 가는 소리.

그리고…….

다른 존재는 들을 수 없는 나직한 목소리가, 귓가에 닿았다.

― 놓치지 마.

“……!”

진태경의 전음(傳音)을 들은 스켈레톤 킹은 깨달았다.

분명 자신을 쓰러트릴 절호의 기회임에도, 왜 어떤 마법도 날아들지 않았는지.

동시에 공기를 타고 은밀하게 전해지는 이 기운이 무엇인지.

‘텔레포트!’

스켈레톤 킹의 짐작은 사실이었다.

도플갱어는 지금, 혼신의 힘을 다하여 텔레포트 마법진을 그려 내고 있었다.

걸출한 대마도사의 영혼을 취했다는 것에 대한 안도와 후회를 동시에 느끼며.

‘이런 개 같은……!’

도플갱어의 본질이 마력과 친숙한 몬스터라고는 하나, 지금은 한낱 인간의 몸.

당장 진태경이라는 괴물에게서 완전히 멀어지기 위해 텔레포트 마법을 마법진 없이 사용한다면, 부활의 기회조차 없이 먼지처럼 바스라질 것이 뻔했다.

스아아아.

허공을 내저은 손을 따라 흘러나온 마나가 도플갱어의 전신을 조금씩 휘감았다.

비록 마법진을 완성하기까지는 약간의 시간이 필요했지만, 위험성은 절반 이상으로 줄어든다.

육체가 흔적도 없이 산산이 분해되는 수준에서, 상반신 정도는 건질 수 있을 정도로.

하지만 도플갱어가 살아남기에는 그것만으로도 충분했고, 기나긴 세월을 살아온 심연의 괴물은 자신의 소멸이 걸린 이 신중한 문제에 방해꾼이 끼어드는 것을 결코 용납할 수 없었다.

쉭, 카앙!

순식간이었다.

날카로운 파공성과 함께 날아든 뼛조각이, 빠르게 펼쳐 낸 방어 마법에 막혀 튕겨 나간 것은.

쉬쉬쉬쉭! 카가강!

얼마 남지 않은 완성을 코앞에 두고 있던 도플갱어가, 쉼없이 뼛조각을 쏘아 보내는 스켈레톤 킹의 모습에 얼굴을 일그러트렸다.

‘뭐지? 아직 지속 시간은 한참 남아 있을 텐데.’

대마도사의 기억에 따르면 마법은 완벽했고, 허점을 정확하게 찔러 시야를 뺏었다.

전투에서 시력을 상실한다는 것은 두 다리를 쓰지 못하는 것과 같다.

도플갱어가 굳이 더 나서서 스켈레톤 킹을 무력화시키지 않은 건 바로 그 때문이었다.

만만치 않은 강자일뿐더러, 무슨 짓을 더 벌일지 모르는 진태경을 피해 멀리 도망치는 것이 더욱 급선무였으니까.

그러나 지금 이 순간, 스켈레톤 킹의 움직임은 도플갱어의 예상을 한참이나 벗어나고 있었다.

콰창!

가파른 속도와 강한 힘. 그리고 무엇보다 정확한 방향으로 쏘아진 뼛조각이 마침내 방어 마법을 산산조각 낸다.

찰나의 틈을 타 블링크 마법으로 위험을 벗어난 도플갱어의 눈동자에 당혹감이 어렸다.

‘도대체 어떻게…….’

상대의 움직임 하나하나를 보면 알 수 있다. 저건 확신이 없다면 할 수 없는 공격들이다.

분명 라이트 마법에 직격당했음에도, 지금의 스켈레톤 킹은 한 치의 망설임도 없이 공격을 이어 나가고 있었다.

팟.

흐릿해진 신형이 공간을 가로질러 쇄도한다. 동시에 황금빛 마력을 머금은 검신이 유려한 선을 그렸다.

주인의 뜻대로.

그리고 주인의 귓가에 닿은 누군가의 목소리대로.

― 좌로 일 보(步).

그 순간.

슈확!

거침없이 쏘아지던 스켈레톤 킹의 신형이 흔들렸다.

흩날리는 금빛 머리카락 사이를 스쳐 지나간 얼음의 창이 돌무더기를 강타했다.

쾅! 쩌저적!

서늘해진 공기. 스켈레톤 킹은 자신의 감각과, 귓가로 전해지는 전음을 따라 움직였다.

― 우로 삼 보. 횡격.

서걱!

덩굴 식물을 불러내 상대를 속박하는 마법인 바인딩(Binding).

그 쇠사슬처럼 두껍고 단단한 식물의 줄기가 단번에 끊어지고.

― 숙여.

수십여 발의 매직 미사일이 텅 빈 허공을 관통했다.

― 십 보 전진. 꿰뚫어 버려.

퍼퍼펑!

대마도사의 힘으로 펼친 마법답게, 위력은 강력하고 폭발은 화려하다.

그러나 그 어떤 마법도 스켈레톤 킹에게 닿지 못했고, 도플갱어는 어느새 불과 열 걸음 안까지 들이닥친 그의 모습을 보며 헛숨을 삼켰다.

‘벌써……!’

마치 귀신에 홀린 듯한 기분이었다.

스켈레톤 킹은 쉴 새 없이 뼛조각을 쏘아 보내며 마법진의 완성을 방해했고, 공격 마법을 피하거나 베어 가르며 모조리 파훼했다.

‘이 정도였나? 저 변종이?’

하지만 도플갱어가 떠올린 의문은, 스켈레톤 킹의 초점 잃은 눈동자를 본 순간 흔적도 없이 사라졌다.

그리고 찬물을 뒤집어쓴 듯한 충격이, 의문의 빈자리를 채웠다.

‘놈이었어. 처음부터.’

도대체 무슨 수를 쓴 걸까.

당장이라도 쓰러질 것처럼 간신히 서 있으면서, 어떻게 자신을 이렇게까지 무력화시킬 수 있었던 걸까.

도플갱어는 혼란과 두려움을 동시에 느끼며 마나를 끌어 올렸다.

블링크 마법.

그 찰나의 깜빡임이 다시 한번 스켈레톤 킹과 거리를 벌렸다.

아니, 벌렸다고 생각했다.

수 미터의 공간이 사라지기 직전, 블링크 마법의 발현보다 앞서 스켈레톤 킹의 귓가에 닿은 음성이 아니었다면 분명 그렇게 되었을 것이다.

― 다섯 시 방향. 나아가면서…….

도플갱어의 신형이 흐릿해지기 전, 방향을 틀어 쏘아져 온 스켈레톤 킹이 검을 들어 올렸다.

솨아아아.

느려진 세상 속. 찬란히 빛나는 황금빛 마력이 파도처럼 솟아오른다.

뒤이어 들려온 목소리와 함께 공간을 갈랐다.

― 하늘부터 땅끝까지. 내리그어.

슈확!

황금빛 섬광이, 조금 전까지만 하더라도 텅 빈 공간이었던 그곳에 우뚝 서 있던 심연의 괴물을 갈랐다.

서걱, 푸화악!

정수리로 시작하여 가랑이까지 이어진 붉은 선.

이내 터져 나온 핏물과 함께, 탄식과도 같은 전음이 스켈레톤 킹의 귓가에 닿았다.

― 아, 시발. 맞다. 내 경험치.
```

## Final English reading copy

```markdown
# Chapter 828

Fear comes in different kinds and degrees.

Some people spend their whole lives afraid of water because they fell into a valley stream as children. Those who’ve lived through an earthquake carry trauma like a brand.

But the greatest and deepest fear of all is fear of the unknown.

A realm no one has ever seen—or even imagined.

That’s what the unknown is.

The universe and the deep sea, beyond the reach of even humanity, with its brilliant civilization built on science and magic.

And now, in this very moment, a single streak of fire tearing everything around it to shreds.

*BOOOOM!*

It was like a storm.

A storm of fire, so razor-sharp it made your skin crawl, turning everything it touched to ash.

The Doppelganger stared at the scene in stunned silence.

Blue-white flames, pouring out suffocating heat, stained its pupils red.

*SHWAAK!*

Tearing. Ripping. Slicing.

The wind shrieked. The Golems it had spent three years painstakingly shaping burst apart like fireworks.

Limbs of massive, solid rock and weapons crashing down hard enough to split the earth—none of it mattered.

*Fwoosh. KRRRACK!*

They melted. They crumbled.

It took only an instant for all seventy-two Golems to become nothing but heaps of rubble. It happened before the Doppelganger could even order them to retreat.

No—that wasn’t quite right. It hadn’t even had time to do that.

The flames tearing through everything hadn’t destroyed only the Golems.

*CRASH!*

A tremendous force raged through the air.

The magic circles, scattering dazzling halos of light, exploded one after another.

The Doppelganger watched in horror as the translucent barrier surrounding it melted like candle wax.

“What the…”

But before it could finish, something hot surged up from deep inside its body, spilling through its throat and into its mouth.

*Hack.*

The Doppelganger spat out a clump of dark red blood. Its pupils trembled.

Knowledge surfaced from Siegfried Bassman’s memories and struck its empty mind.

Mana backlash.

The forced severing of its connection to so many magic circles had sent the energy in its body into a frenzy.

If it hadn’t prepared the magic circles through various conduits and spells, and had instead cast the magic directly, it wouldn’t have been surprising if it had died several times over. The blow was that severe.

*How? How is this possible?*

The Doppelganger gasped for breath and raised its head.

There wasn’t a trace of composure left in its eyes, only shock.

The only thing reflected in them was one human who seemed as unknowable as the unknown itself.

*Jin Taekyung.*

There he was.

He stood tall, gripping a silver spear that glowed white as the Golems’ remains rained down over his head.

Then, through the halo of light left behind by the magic circles melted by the flames, the Doppelganger saw a predator staring straight at it.

“Say that again.”

His voice sounded like it might break at any moment, yet boiled like lava as it pierced the Doppelganger’s ears.

His unsteady footsteps approached, as if he might collapse at any moment.

*Step.*

It was strange.

The whole place was filled with thunderous noise. The temple, stripped of its pillars, was slowly collapsing, and the rocks that had once been Golems were scattering in every direction…

*Step.*

And yet the footsteps of that small human sounded like thunder. The sound of his voice made every hair on the Doppelganger’s body stand on end.

“Who exactly is the master here?”

“……!”

The Doppelganger had to swallow a scream that was rising unbidden between its lips.

Clear fear was carved into its eyes as it stared at Jin Taekyung.

A monster. That human was a monster.

One who surpassed expectations and limits by an impossible distance, every single time.

After dying countless times on the battlefield, the Doppelganger had long since abandoned its contempt for Jin Taekyung.

It had let go of everything and judged the situation coldly. This time, it had been certain.

Once it reached its destination, everything would go smoothly.

Jin Taekyung would never catch it.

But it had been wrong.

The Doppelganger, which had left the battlefield before anyone else, hadn’t known Jin Taekyung had reached an even higher realm in that brief time.

Now that it had realized the truth, it was too late.

*If I waste even a little more time here… then I’m finished.*

Erasure. Forever.

At the thought, a cold fear crawled up its spine.

The movement that followed was instinct, not reason.

The Doppelganger burned through the souls it had left without hesitation. It healed the body mangled by mana backlash, then gathered the energy that had once again filled it to the brim into both hands and unleashed it.

At the inhuman monster approaching it.

At Jin Taekyung.

*FWOOSH!*

The instant a blinding flash burst forth—

“No!”

The Skeleton King, who had been charging at the Doppelganger a step ahead of him, hurriedly twisted around and put himself in the flash’s path.

*POP!*

The Skeleton King in his usual state wouldn’t even have snorted at it.

For all his bluster, he accepted that Jin Taekyung was stronger than him.

But…

*Right now, I’m the only one who can protect that devious human.*

Protect him. Even if it meant putting himself in danger.

For the Skeleton King, it had become the most natural thing in the world.

Why?

At some point, he’d stopped thinking about the reason. Friends didn’t need a reason.

*SHWAA!*

The Skeleton King swung the Hero’s Sword down.

Golden magical power, bright as sunlight and strangely unlike magic, split the flash.

No.

The moment he thought he’d cut it, the flash passed through the blade like mist and swelled like a balloon.

*WHUM.*

*What the—*

Before the question in his mind could finish, a light far brighter than the last filled the Skeleton King’s vision.

*FWOOSH!*

The whole world turned white.

In that blinding flash, which would have instantly robbed an ordinary human of their sight, the Skeleton King belatedly remembered the answer to his question.

*Damn it.*

There was no doubt.

This was Light magic, something even mid- and lower-level mages could cast with ease.

A simple convenience spell, rarely used in actual combat because it had little killing power and produced only a faint light.

At least, that was what the Skeleton King knew. Hunters accepted it as established fact, too.

If he’d known that Siegfried Bassman, a scholarly Grand Mage, had shut himself away in his hideout to study countless spells, and had increased the power and usefulness of Light magic by several levels, he could have prepared for it.

But the milk had already been spilled. The painful mistake was enough to make the Skeleton King’s heart sink.

*I can’t see. Anything.*

He hadn’t lost his sight completely.

The Skeleton King was undead, after all, with a vitality that couldn’t be compared to that of a human made of flesh and blood.

But even temporarily losing his sight while fighting a powerful enemy like the Doppelganger—and having to protect someone else at the same time—was a mistake he couldn’t take back.

*It planned this from the start. It knew I’d step in…*

In the white world where he couldn’t see a thing, the Skeleton King raised his sword. With his sight gone, his hearing took in everything around him.

The roar of rubble crashing down a moment later.

An unfamiliar cracking sound from somewhere above.

And then…

A low voice, too quiet for any other being to hear, reached his ear.

—Don’t let it get away.

“……!”

The Skeleton King heard Jin Taekyung’s Sound Transmission and understood.

Why no magic had come flying at him, even though this was the perfect chance to knock him down.

And what the energy being carried quietly through the air was.

*Teleport!*

The Skeleton King’s guess was right.

The Doppelganger was now pouring all its strength into drawing a Teleport magic circle.

It felt both relief and regret at having taken the soul of an exceptional Grand Mage.

*You piece of shit…!*

The Doppelganger’s nature might be that of a monster familiar with magical power, but right now it was in the body of an ordinary human.

If it tried to cast Teleport without a magic circle just to get as far as possible from the monster named Jin Taekyung, it would crumble into dust without even a chance to resurrect.

*Fwoosh.*

Mana flowed from the Doppelganger’s hand as it swept through the air, slowly wrapping around its body.

Completing the magic circle would take a little time, but it would cut the risk by more than half.

Instead of its body being disintegrated without a trace, it might at least save its upper half.

That was more than enough for the Doppelganger to survive. And the deep-abyss monster, which had lived for countless ages, would never allow an intruder to interfere with this careful matter of its own survival.

*Whoosh. CLANG!*

It happened in an instant.

A bone fragment shot in with a sharp whistle and was deflected by the defensive magic the Doppelganger hurriedly cast.

*SH-SH-SH-SH! CLANG!*

The Doppelganger’s face twisted as it watched the Skeleton King fire bone fragments without pause, with the magic circle almost complete.

*What? The effect should last much longer.*

According to the Grand Mage’s memories, the spell was perfect. It had taken away the Skeleton King’s sight by striking the weakness precisely.

Losing your sight in battle was like losing the use of both legs.

That was exactly why the Doppelganger hadn’t bothered trying to disable the Skeleton King any further.

He was no pushover, and escaping as far away as possible from Jin Taekyung—who might do who knew what next—was more urgent.

But right now, the Skeleton King’s movements were far beyond anything the Doppelganger had expected.

*CRASH!*

The bone fragments, shot with incredible speed and force—and, above all, in a precise direction—finally shattered the defensive magic.

The Doppelganger’s eyes widened in confusion as it escaped the danger with a Blink spell, taking advantage of that instant opening.

*How the hell…*

It could tell from each of its opponent’s movements. Those attacks weren’t possible without certainty.

Even though the Skeleton King had taken the full force of the Light magic, he continued his attacks without the slightest hesitation.

*POP.*

His hazy form shot across the space. At the same time, the golden magical power coating his sword traced a graceful arc.

As the sword’s wielder willed.

And as the voice in his ear directed.

—One step left.

At that moment—

*SHWAAK!*

The Skeleton King’s unhesitating charge wavered.

An ice spear grazed the golden hair whipping through the air and slammed into a pile of rubble.

*BOOM! CRACK-CRACK!*

The air turned cold. The Skeleton King followed his senses and the Sound Transmissions reaching his ears.

—Three steps right. A horizontal slash.

*SHHK!*

Binding magic, which summoned vines to ensnare the target.

The thick, tough vines, like chains, were severed in an instant.

—Duck.

Dozens of Magic Missiles shot through empty air.

—Ten steps forward. Pierce it.

*BOOM-BOOM-BOOM!*

As expected of magic cast with a Grand Mage’s power, it was strong, and the explosions were spectacular.

But not a single spell touched the Skeleton King. The Doppelganger swallowed a startled breath as he closed to within ten steps.

*Already…!*

The Doppelganger felt as though it had been bewitched by a ghost.

He fired bone fragments without pause, disrupting the completion of the magic circle, and dodged or cut through every attack spell, foiling them all.

*Was he always this strong? That mutant?*

But the question disappeared without a trace the moment the Doppelganger saw the Skeleton King’s unfocused eyes.

A shock like a bucket of cold water filled the empty space where the question had been.

*It was him. From the start.*

What on earth had he done?

How could he be barely standing, as if he were about to collapse at any moment, and still render the Doppelganger this helpless?

The Doppelganger felt both confusion and fear as it gathered its mana.

Blink magic.

That instant flicker put distance between it and the Skeleton King once again.

Or so it thought.

Just before several meters of space disappeared, the voice that reached the Skeleton King’s ear came before the Blink spell could take effect. Without it, that was certainly what would have happened.

—Five o’clock. Move forward and—

Before the Doppelganger’s form could blur, the Skeleton King changed direction and charged, raising his sword.

*Fwooooosh.*

In the slowed world, brilliant golden magical power surged like a wave.

Then, with the voice that followed, it cleaved through space.

—From the sky to the ends of the earth. Bring it down.

*SHWAAK!*

A streak of golden light cleaved the deep-abyss monster standing in the spot that had been empty only moments before.

*SHHK. FWOOSH!*

A red line ran from the crown of its head down to its crotch.

Blood burst out, and a Sound Transmission that sounded like a groan reached the Skeleton King’s ear.

—Ah, shit. Right. My EXP.
```
